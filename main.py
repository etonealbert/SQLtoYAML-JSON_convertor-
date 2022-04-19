import pandas as pd
from arghttp import req
from ruamel.yaml import YAML

#Path to the file
json_file = r'C:\Users\Albert\DataEngeneering\JSON\Goods.json'
yaml_file = r'C:\Users\Albert\DataEngeneering\YAML\Goods.yaml'

def main():
    prefix = 'Booker_Test.dbo.'
    goods_df = pd.read_json(req(f'select ID, Name from {prefix}Shops'))

    convert_json(goods_df)

    convert_yaml(goods_df)

def convert_json(goods_df):

    with open(json_file, 'w', encoding='utf-8') as file:
        goods_df.to_json(file, force_ascii=False, indent=1)

def convert_yaml(goods_df):

    yaml = YAML(typ="safe")
    yaml.default_flow_style = False

    with open(yaml_file, "w", encoding="utf-8") as o:
        yaml.dump(goods_df.to_dict(), o)




if __name__ == '__main__':
    main()








