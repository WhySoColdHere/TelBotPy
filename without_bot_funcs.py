from random import randint


# 1
def random_photo():
    photo_list = ['photo_with_tyan/tyan1.jpg',
                  'photo_with_tyan/tyan2.jpg',
                  'photo_with_tyan/tyan3.jpg',
                  'photo_with_tyan/tyan4.jpg',
                  'photo_with_tyan/tyan5.jpg',
                  'photo_with_tyan/tyan6.jpg',
                  'photo_with_tyan/tyan7.jpg',
                  'photo_with_tyan/tyan8.jpg',
                  'photo_with_tyan/tyan9.png',
                  'photo_with_tyan/tyan10.jpg']
    return open(photo_list[randint(0, 9)], 'rb')


# 2
id_btn_mass = ['btn1', 'btn2', 'btn3', 'btn4', 'btn5', 'btn6',
               'btn7', 'btn8', 'btn9', 'btn10', 'btn11', 'btn12',
               'btn13', 'btn14', 'btn15', 'btn16',
               'btn17']


# 3
def but_hor_func(x_call_data, y_id_mass, z_call, q_horo, r_ret, q_money):
    for i in range(0, 16):
        if (x_call_data == y_id_mass[i]) and (i < 12):
            r_ret(z_call.message, q_horo[i])
        elif (x_call_data == y_id_mass[i]) and (i >= 12):
            r_ret(z_call.message,
                  f'<b>Code:</b> <em>{q_money[i - 12][0]}</em>\n<b>Nominal</b>: {q_money[i - 12][1]}\n<b>Value</b>: {q_money[i - 12][2]}')
