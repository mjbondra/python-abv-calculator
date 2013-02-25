abv_multiplier = 131
#abv_multiplier = 129

try:
    from Gui import *
    gui_present = True
except:
    gui_present = False

def calculate_abv(og,fg):
    return str('%.2f' % (abv_multiplier * (float(og) - float(fg))))

def calculate_attenuation(og,fg):
    return str('%.2f' % (100 * (1 - (float(fg) - 1)/(float(og) - 1))))

def results_controller():
    try:
        abv_calculated = calculate_abv(original_gravity.get(),final_gravity.get())
        attenuation_calculated = calculate_attenuation(original_gravity.get(),final_gravity.get())
        abv.delete(0, END)
        abv.insert(0,  abv_calculated + '%')
        attenuation.delete(0, END)
        attenuation.insert(0, attenuation_calculated + '%')
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
    main_window.bu(text='Calculate Attenuation and ABV', command=results_controller)
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
        try:
            abv_calculated = calculate_abv(original_gravity,final_gravity)
            attenuation_calculated = calculate_attenuation(original_gravity,final_gravity)
            print 'Attenuation: ' + attenuation_calculated + '%'
            print 'Alcohol by Volume: ' + abv_calculated + '%\n'
        except:
            print 'Error with your inputs'

