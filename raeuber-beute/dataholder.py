# -*- coding: utf-8 -*-
from predatorpreycalculator import *

class DataHolder(object):
    """ Just a thin wrapper over a dictionary that holds integer 
        data series. Each series has a name and a list of numbers 
        as its data. The length of all series is assumed to be
        the same.
        
        The series can be read from a CSV file, where each line
        is a separate series. In each series, the first item in 
        the line is the name, and the rest are data numbers.
    """
    def __init__(self, filename=None):
        self.load_from_file(filename)
        self.simulator = PredatorPreyCalculator()
    
    def calculate_from_values(self):
        self.data = {}
        self.names = ["Predator", "Prey"]
                       
        r, b = self.simulator.calculate()
        
        self.data["Predator"] = map(float, r[1:])
        self.data["Prey"] = map(float, b[1:])
        self.datalen = len(r[1:])       
    
    def load_from_file(self, filename=None):
        self.data = {}
        self.names = ["Predator", "Prey"]
        
        if filename:
            for line in csv.reader(open(filename, 'rb')):
                self.data[line[0]] = map(float, line[1:])
                self.datalen = len(line[1:])
    
    def series_names(self):
        """ Names of the data series
        """
        return self.names
    
    def series_len(self):
        """ Length of a data series
        """
        return self.datalen
    
    def series_count(self):
        return len(self.data)

    def get_series_data(self, name):
        return self.data[name]