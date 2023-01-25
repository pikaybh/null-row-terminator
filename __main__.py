import os
import pandas as pd


def csv_finder(_wdir: str) -> list:
    '''
    listdir 안에서 .csv 확장자인 파일만 찾아냄
    '''
    file_list = os.listdir(_wdir)
    csv_list = [file for file in file_list if file.endswith(".csv")]
    return csv_list

def filter(_df: object) -> None:
    '''
    값이 "." 인 데이터를 포함하는 행 삭제
    '''
    for i in list(_df):
        _index = _df[_df[i] == "."].index
        _df.drop(_index, inplace = True)

def result_file_name(_name: str) -> str:
    '''
    정제된 csv 파일 저장할 이름
    e.g. "<<name>>_result.csv"
    '''
    _name, ext = _name.split(".")
    _name = _name + "_result." + ext
    return _name

def process(_csv_file: str) -> None:
    '''
    csv 파일로 부터 dataframe을 만들어서 정제하고, 결과.csv 저장
    '''
    df = pd.read_csv(_csv_file)
    filter(df)
    df.to_csv("results/" + result_file_name(_csv_file), index = False)


if __name__ == "__main__":
    # 현재 디렉토리
    csv_list = csv_finder("./")
    for csv in csv_list:
        process(csv)