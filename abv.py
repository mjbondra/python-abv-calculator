try:
    from Gui import *
    gui_present = True
except:
    gui_present = False

def calculate_abv_attenuation():
    try:
        abv_calculated = str(131 * (float(original_gravity.get()) - float(final_gravity.get())))
        attenuation_calculated = str(100 * (1 - (float(final_gravity.get()) - 1)/(float(original_gravity.get()) - 1)))
        abv.delete(0, END)
        abv.insert(0, abv_calculated[:4] + '%')
        attenuation.delete(0, END)
        attenuation.insert(0, attenuation_calculated[:5] + '%')
    except:
        display_error()

def display_error():
    error_window = Gui()
    error_window.title('Error')
    error_window.la('')
    error_window.gr(cols=3)
    error_window.la('    ')
    error_window.la('Fix your inputs')
    error_window.la('    ')
    error_window.endgr()
    error_window.la('')

if gui_present:
    main_window = Gui()
    main_window.title('Attenuation and ABV Calculator')
    main_window.la('')
    main_window.gr(cols=3)
    main_window.la('Original Gravity:')
    original_gravity = main_window.en(text='')
    main_window.la('    ')
    main_window.la('Ending Gravity:')
    final_gravity = main_window.en(text='')
    main_window.la('    ')
    main_window.endgr()
    main_window.la('')
    main_window.gr(cols=3)
    main_window.la('    ')
    main_window.bu(text='Calculate Attenuation and ABV', command=calculate_abv_attenuation)
    main_window.la('    ')
    main_window.endgr()
    main_window.la('')
    main_window.gr(cols=3)
    main_window.la('Attenuation:')
    attenuation = main_window.en(text='')
    main_window.la('    ')
    main_window.la('Alcohol By Volume:')
    abv = main_window.en(text='')
    main_window.la('    ')
    main_window.endgr()
    main_window.la('')

    main_window.mainloop()
else:
    print 'type \'q\' or \'quit\' to quit'
    while True:
        original_gravity = raw_input('Original Gravity: ')
        if original_gravity[0].lower() == 'q':
            break
        final_gravity = raw_input('Ending Gravity: ')
        if final_gravity[0].lower() == 'q':
            break
        print ''
        abv_calculated = str(131 * (float(original_gravity) - float(final_gravity)))
        attenuation_calculated = str(100 * (1 - (float(final_gravity) - 1)/(float(original_gravity) - 1)))
        print 'Attenuation: ' + attenuation_calculated[:5] + '%'
        print 'Alcohol by Volume: ' + abv_calculated[:4] + '%\n'

