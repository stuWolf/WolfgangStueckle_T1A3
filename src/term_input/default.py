
# seed the list of parameters put of the main file
def default_values():
    step1 = {"name": "Start Balance", "value": 1000} 
    step2 = {"name": "Monthly Deposit", "value": 0}
    step3 = {"name": "Annual interest", "value": 18}
    step4 = {"name": "Compound rate", "value": 'monthly'}
    step5 = {"name": "Time in Years", "value": 10}
    default_values = [step1, step2, step3, step4, step5]
    return default_values