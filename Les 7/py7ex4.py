def ticker(filename):
    content = open(filename, 'r')
    reader = content.readlines()
    Lijst = []
    for Ticker_or_company in reader:
        Lijst.append(Ticker_or_company.strip().split(':'))
    company_and_ticker_Dictionary = {}
    for Ticker_or_company in Lijst:
        key = Ticker_or_company[0]
        value = Ticker_or_company[1]
        company_and_ticker_Dictionary[key] = value
    print(company_and_ticker_Dictionary)

    Lijst2 = []
    for Ticker_or_company in company_and_ticker_Dictionary.values():
        Lijst2.append(Ticker_or_company)
    company = input('Voer een bedrijfsnaam in: ')
    if company in company_and_ticker_Dictionary:
        print(company_and_ticker_Dictionary[company])
    elif company not in company_and_ticker_Dictionary:
        for Ticker_or_company,y  in company_and_ticker_Dictionary.items():
            if y == company:
                print(Ticker_or_company)
ticker('ticker.txt')