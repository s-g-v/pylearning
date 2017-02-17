#!/usr/bin/env python3
import sys
from pandas import read_csv, DataFrame
from sklearn.metrics import roc_auc_score, precision_recall_curve, auc


def read_data(first_file, second_file):
    """Reads series from two cvs files and returns DataFrame object"""
    series1=read_csv(first_file, squeeze=True, header=None)
    series2=read_csv(second_file, squeeze=True, header=None)
    if series1.dtype == 'float64':
        return DataFrame({"Actual":series1,"Expected":series2})
    else:
        return DataFrame({"Actual":series2,"Expected":series1})


def get_metric(data_frame, metric=None):
    """Requires DataFrame object with 'Actual'(provided by algorithm) and 'Expected' columns.
metric - pass 'pr' to calculate area under precision recall curve"""
    if metric == "pr":
        precision, recall, treshold = precision_recall_curve(data_frame.get("Expected"), data_frame.get("Actual"))
        auc_prc = auc(recall, precision)
        return ("AUC_PRC", auc_prc)
    else:
        auc_roc=roc_auc_score(data_frame.get("Expected"), data_frame.get("Actual"))
        return ("AUC_ROC", auc_roc)


if __name__=="__main__":
    data=read_data(sys.argv[1], sys.argv[2])
    metric = "roc" if len(sys.argv) <= 3 else sys.argv[3]
    print(get_metric(data, metric)[1])
