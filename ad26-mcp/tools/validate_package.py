"""Offline publication checks only: no AD, network, subprocess or runtime imports."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))

def validate(value, schema, where='$'):
    if 'const' in schema and (type(value) is not type(schema['const']) or value != schema['const']):
        raise ValueError(where+': const')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(where+': enum')
    types={'object':lambda x:isinstance(x,dict),'array':lambda x:isinstance(x,list),'string':lambda x:isinstance(x,str),'integer':lambda x:type(x) is int,'boolean':lambda x:type(x) is bool,'null':lambda x:x is None}
    if 'type' in schema:
        allowed=schema['type'] if isinstance(schema['type'],list) else [schema['type']]
        if not any(types[t](value) for t in allowed):raise ValueError(where+': type')
    if isinstance(value,dict):
        if any(k not in value for k in schema.get('required',[])):raise ValueError(where+': required')
        props=schema.get('properties',{})
        if schema.get('additionalProperties') is False and set(value)-set(props):raise ValueError(where+': extra keys')
        for k,s in props.items():
            if k in value:validate(value[k],s,where+'.'+k)
    if isinstance(value,list):
        for n,v in enumerate(value):validate(v,schema.get('items',{}),where+'['+str(n)+']')
    if isinstance(value,str):
        if len(value)<schema.get('minLength',0):raise ValueError(where+': length')
        if 'pattern' in schema and not re.search(schema['pattern'],value):raise ValueError(where+': pattern')
    if type(value) is int and value<schema.get('minimum',value):raise ValueError(where+': minimum')
    if 'oneOf' in schema:
        matches=0
        for s in schema['oneOf']:
            try:validate(value,s,where)
            except ValueError:pass
            else:matches+=1
        if matches!=1:raise ValueError(where+': oneOf')

def ascii_params(value):
    if isinstance(value,str) and not value.isascii():raise ValueError('Non-ASCII incoming parameter')
    if isinstance(value,dict):
        for k,v in value.items():ascii_params(k);ascii_params(v)
    if isinstance(value,list):
        for v in value:ascii_params(v)

def main():
    manifest=load(ROOT/'publication.json')
    for path,expected in manifest['files_sha256'].items():
        blob=(REPO/path).read_bytes()
        if hashlib.sha256(blob).hexdigest()!=expected:raise ValueError('Hash mismatch: '+path)
    for p in [*ROOT.rglob('*.json')]:load(p)
    req=load(ROOT/'examples/request.ping.json')
    validate(req,load(ROOT/'schemas/request.schema.json'));ascii_params(req['params'])
    for name in ['response.ping.json','response.error.json','response.geometry.json']:
        validate(load(ROOT/'examples'/name),load(ROOT/'schemas/response.schema.json'))
    geometry=load(ROOT/'examples/response.geometry.json')['data']
    gs=load(ROOT/'schemas/geometry-data.schema.json');validate(geometry,gs)
    kinds=list(geometry['counts'])
    if any(len(geometry[k])>geometry['limit'] for k in kinds):raise ValueError('Array limit')
    if geometry['truncated']!=any(geometry['counts'][k]>geometry['limit'] for k in kinds):raise ValueError('Truncation')
    ids={x['index'] for x in geometry['sheet_symbols']}
    if any(x['sheet_index'] not in ids for x in geometry['sheet_entries']):raise ValueError('Synthetic association')
    commands=load(ROOT/'catalog/commands.json')
    names=[x['name'] for x in commands['commands']]
    if len(names)!=47 or len(set(names))!=47:raise ValueError('Command catalog')
    tools={t for c in commands['commands'] for t in c['standard_mcp_tools']}
    if len(tools)!=5:raise ValueError('Tool count must not equal native command count')
    bad=dict(geometry);bad.pop('pins')
    try:validate(bad,gs)
    except ValueError:pass
    else:raise ValueError('Missing empty array was accepted')
    try:ascii_params({'nested':[chr(0x4e2d)]})
    except ValueError:pass
    else:raise ValueError('Unicode parameter admitted')
    for p in [REPO/'README.md',*ROOT.rglob('*.md')]:
        text=p.read_text(encoding='utf-8')
        if '[[' in text:raise ValueError('Unresolved internal wiki link: '+str(p))
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if target.startswith(('http:','https:','#','mailto:')):continue
            if not (p.parent/target.split('#')[0]).is_file():raise ValueError('Broken link '+target)
    # All fixture paths are synthetic; reject ordinary user-profile paths and credentials.
    for p in [REPO/'README.md',*ROOT.rglob('*')]:
        if not p.is_file() or '__pycache__' in p.parts:continue
        text=p.read_text(encoding='utf-8')
        if re.search(r'[A-Z]:[\\/]+Users[\\/]+(?!Public)',text,re.I):raise ValueError('User path: '+str(p))
        if re.search(r'(?:ghp_|github_pat_)[A-Za-z0-9]{20,}',text):raise ValueError('Credential-like token')
    print('PASS: JSON/schema subset, ASCII admission,47 commands/5 tools, examples, negative cases, links, privacy and publication hashes; no native AD test performed')

if __name__=='__main__':main()
