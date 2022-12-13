import pandas as pd

df = pd.read_csv('comprehension1.csv')
print(list(df.columns.values))

# print(df.to_string())
""" Strictly Necessary Cookies: Cookies that are needed for the website to work properly
Performance Cookies: Cookies that help measure and improve the website features 
Functional Cookies: Cookies that help personalize the website’s services for you
Advertising Cookies: Cookies that are used to deliver personalized advertisements """

# print(df['anonymous analytics'])
for index in df.index:
    # functional: personalized experience, enhanced function, functional
    # if df.loc[index, 'personalized experience'] == "Cookies that help personalize the website's services for you":
    #     df.loc[index, 'personalized experience'] = '1'
    # elif df.loc[index, 'personalized experience'] != "Cookies that help personalize the website's services for you":
    #     df.loc[index, 'personalized experience'] = '0'
    
    # if df.loc[index, 'enhanced function'] == "Cookies that help personalize the website's services for you":
    #     df.loc[index, 'enhanced function'] = '1'
    # elif df.loc[index, 'enhanced function'] != "Cookies that help personalize the website's services for you":
    #     df.loc[index, 'enhanced function'] = '0'
    
    # if df.loc[index, 'functional'] == "Cookies that help personalize the website's services for you":
    #     df.loc[index, 'functional'] = '1'
    # elif df.loc[index, 'functional'] != "Cookies that help personalize the website's services for you":
    #     df.loc[index, 'functional'] = '0'


    # # targeting: personalized advertising, targeting
    # if df.loc[index, 'personalized advertising'] == "Cookies that are used for delivering personalized advertisements":
    #     df.loc[index, 'personalized advertising'] = '1'
    # elif df.loc[index, 'personalized advertising'] != "Cookies that are used for delivering personalized advertisements":
    #     df.loc[index, 'personalized advertising'] = '0'
    
    # if df.loc[index, 'targeting'] == "Cookies that are used for delivering personalized advertisements":
    #     df.loc[index, 'targeting'] = '1'
    # elif df.loc[index, 'targeting'] != "Cookies that are used for delivering personalized advertisements":
    #     df.loc[index, 'targeting'] = '0'


    # # strictly necessary: strictly necessary, required, essential function
    # if df.loc[index, 'strictly necessary'] == "Cookies that are needed for the website to work properly":
    #     df.loc[index, 'strictly necessary'] = '1'
    # elif df.loc[index, 'strictly necessary'] != "Cookies that are needed for the website to work properly":
    #     df.loc[index, 'strictly necessary'] = '0'

    # if df.loc[index, 'required'] == "Cookies that are needed for the website to work properly":
    #     df.loc[index, 'required'] = '1'
    # elif df.loc[index, 'required'] != "Cookies that are needed for the website to work properly":
    #     df.loc[index, 'required'] = '0'

    # if df.loc[index, 'essential function'] == "Cookies that are needed for the website to work properly":
    #     df.loc[index, 'essential function'] = '1'
    # elif df.loc[index, 'essential function'] != "Cookies that are needed for the website to work properly":
    #     df.loc[index, 'essential function'] = '0'


    # performance: anonymous analytics, aggregated analytics, performance
    if df.loc[index, 'Analytics'] == "Cookies that help measure and improve website features" or df.loc[index, 'Analytics'] == 'Cookies that are needed for collecting certain metrics':
        df.loc[index, 'Analytics'] = '1'
    elif df.loc[index, 'Analytics'] != "Cookies that help measure and improve website features" or df.loc[index, 'Analytics'] != 'Cookies that are needed for collecting certain metrics':
        df.loc[index, 'Analytics'] = '0'
    
    if df.loc[index, 'Anonymous metrics'] == "Cookies that help measure and improve website features" or df.loc[index, 'Anonymous metrics'] == 'Cookies that are needed for collecting certain metrics':
        df.loc[index, 'Anonymous metrics'] = '1'
    elif df.loc[index, 'Anonymous metrics'] != "Cookies that help measure and improve website features" or df.loc[index, 'Anonymous metrics'] != 'Cookies that are needed for collecting certain metrics':
        df.loc[index, 'Anonymous metrics'] = '0'
    
    if df.loc[index, 'Statistics'] == "Cookies that help measure and improve website features" or df.loc[index, 'Statistics'] == "Cookies that are needed for collecting certain metrics":
        df.loc[index, 'Statistics'] = '1'
    elif df.loc[index, 'Statistics'] != "Cookies that help measure and improve website features" or df.loc[index, 'Statistics'] != "Cookies that are needed for collecting certain metrics":
        df.loc[index, 'Statistics'] = '0'

df.to_csv('cleancomprehension1.csv')