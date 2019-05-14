import pandas as pd
import numpy as np
from statsmodels.tsa.ar_model import AR
import matplotlib.pyplot as plt

input_path = '/Users/adityachandra/Desktop/CashFlow/input/Input.csv'
output_path = '/Users/adityachandra/Desktop/CashFlow/output/Output.csv'
dataset_path = '/Users/adityachandra/Desktop/CashFlow/Dataset/Cash-inflow.csv'
report_path = '/Users/adityachandra/Desktop/CashFlow/output/Forecast_Report.png'

def cashflow_forecast():
    #input_path for CSV
    df=pd.read_csv(input_path)
    df['Total'] = df['Inflow'] - df['Loan'] - df['OutFlow']
    #output_path for CSV
    df.to_csv(output_path,index=False)
    loan_val = df['Loan'].values

    #path for loading dataset
    inp_df = pd.read_csv(dataset_path,index_col='Date')
    inp_df.index = pd.to_datetime(inp_df.index)
    data = list(inp_df.columns)
    data = data[0:4]
    pred = []
    j=0
    for i in data:
        model = AR(inp_df[i].values)
        model_fit = model.fit()
        pred.append(model_fit.predict(len(inp_df[i]),len(inp_df[i])+30))

    bank_val = list(inp_df['BANK'])
    bank_model = AR(inp_df['BANK'].values)
    bank_model_fit = bank_model.fit()
    bank_pred = bank_model_fit.predict(len(bank_val),len(bank_val)+30,dynamic=True)
    bank_forecast = bank_model_fit.predict(len(bank_val),len(bank_val),dynamic=True)

    dict = {'Firm-A':pred[0],'Firm-B':pred[1],'Firm-C':pred[2],'Firm-D':pred[3],'BANK':bank_pred}
    new_df = pd.DataFrame(dict)
    date_rng = date_rng = pd.date_range(start='03/02/2019', periods=31)
    new_df['Date'] = date_rng
    new_df=new_df.set_index('Date')
    report = new_df.plot(kind='line',title='CashFlow Forecast for next 30 days',linewidth=3,fontsize=14,figsize=(15, 10)).get_figure()
    #output_path for report
    report.savefig(report_path)
    # plt.show()

    closing_bal = inp_df.ix[-1].values
    predicted_days = []
    for i in range(0,len(loan_val)):
        result = pred[i]-closing_bal[i]

        idx = (result - loan_val[i]).argmin()
        if result[idx] < 0:
            print("Money "+str(loan_val[i])+" Number of days 30")
            predicted_days.append(30)
        else :
            print("Money "+str(loan_val[i])+" Number of days "+str(idx + 1))
            predicted_days.append(idx.item()+1)

    loan = loan_val.tolist()
    output_val = { 'Bank':int(bank_forecast[0].item()),\
                   'Alpha':{'day':predicted_days[0],'money':loan[0]},\
                   'Beta':{'day':predicted_days[1],'money':loan[1]},\
                   'Gamma':{'day':predicted_days[2],'money':loan[2]},\
                   'Delta':{'day':predicted_days[3],'money':loan[3]}}
    print(output_val)
    return output_val
