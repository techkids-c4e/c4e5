while True:
    n=input('How much do you want to pump?')
    t=float(input('what time is it?'))
    if (t>=5 and t<=7) or (t>=18 and t<=20):
        print('horey!!!water is coming')
        if n=='full':
            print('water is full')
        else:
            print('only one half')
    else:
        print('oupsss.can not pump')
