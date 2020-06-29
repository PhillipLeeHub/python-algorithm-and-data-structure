'''
Income tax brackets are ranges of numbers with a percentage associated to each range.

For example, we might have income tax brackets defined as follows:

0         10,000    10%
10,001    25,000    13%
25,001    50,000    15%
50,001    \infty    20%

To calculate someone's tax obligation on their earnings, we take the percentage associated
to each tax bracket from their earnings in that range. For example:

1. If someone's earnings are $56,000, their tax obligation is:

(10,000 * 0.10) + (15,000 * 0.13) + (25,000 * 0.15) + (6,000 * 0.20) = 7,900

2. If someone's earnings are $36,000, their tax obligation is:

(10,000 * 0.10) + (15,000 * 0.13) + (11,000 * 0.15) + (0 * 0.20) = 4,600

Write a funciton that computes someones tax obligation, given their earnings and a data structure that represents the tax brackets.
'''     
def taxCal(earnings, taxList):
     result_tax = 0
     
     for _min, _max, tax_rate in taxList:
        if earnings < _min:
            continue
        elif _min <= earnings <= _max:
            result_tax+=(earnings - _min) * tax_rate
     
        else: 
            result_tax+=(_max - _min) * tax_rate
     return result_tax

taxList = [
    (0, 10000, .1), 
    (10000, 25000, .13), 
    (25000, 50000, .15), 
    (50000, 100000000, .2)]
     
earnings_1 = 56000
earnings_2 = 36000

# print('Earnings 1: ', taxCal(earnings_1, taxList))
# print('Earnings 2: ', taxCal(earnings_2, taxList))


preTaxListBin = [
    (0, 10000, .1), 
    (10000, 25000, .13), 
    (25000, 50000, .15), 
    (50000, 100000000, .2)]

def genTaxList(preTaxListBin):
    result_list = []
    running_sum = 0
    for _min, _max, tax_rate in taxList:        
        
        result_list.append((_min, _max, tax_rate, running_sum))
        running_sum+= (_max -_min) * tax_rate
        
    return result_list

def taxCalBin(earnings, taxListBin):
    l,r = 0, len(taxListBin)
    result_tax = 0
    
    while(l<=r):
        mid = l + (r-l)//2
        
        _min, _max, tax_rate, acc_tax = taxListBin[mid]
        
        if _min <= earnings <= _max:
            result_tax+=acc_tax + (earnings - _min) * tax_rate
            break
        
        # More
        elif earnings > _max:
            l = mid + 1
            
        # Less
        else: 
            r = mid - 1
            
            
    return result_tax
        
      
postTaxListBin = genTaxList(preTaxListBin)
tax_results_1 = taxCalBin(earnings_1, postTaxListBin)
tax_results_2 = taxCalBin(earnings_2, postTaxListBin)
print(tax_results_1)
print(tax_results_2)
        
        
        
'''
 income, zip
 income, zip
 
 
 zip -> sum(taxes)
 12345 - 10000
 33345 - 54321
 
 00000 - 10000 => distSys01   => 
 10000 - 20000 => distSys02
 {
    'zip':
 }
 '''       
    
    
    
    
