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
    if x_call_data == y_id_mass[0]:
        r_ret(z_call.message, q_horo[0])
    elif x_call_data == y_id_mass[1]:
        r_ret(z_call.message, q_horo[1])
    elif x_call_data == y_id_mass[2]:
        r_ret(z_call.message, q_horo[2])
    elif x_call_data == y_id_mass[3]:
        r_ret(z_call.message, q_horo[3])
    elif x_call_data == y_id_mass[4]:
        r_ret(z_call.message, q_horo[4])
    elif x_call_data == y_id_mass[5]:
        r_ret(z_call.message, q_horo[5])
    elif x_call_data == y_id_mass[6]:
        r_ret(z_call.message, q_horo[6])
    elif x_call_data == y_id_mass[7]:
        r_ret(z_call.message, q_horo[7])
    elif x_call_data == y_id_mass[8]:
        r_ret(z_call.message, q_horo[8])
    elif x_call_data == y_id_mass[9]:
        r_ret(z_call.message, q_horo[9])
    elif x_call_data == y_id_mass[10]:
        r_ret(z_call.message, q_horo[10])
    elif x_call_data == y_id_mass[11]:
        r_ret(z_call.message, q_horo[11])
    elif x_call_data == y_id_mass[12]:
        r_ret(z_call.message,
              f'<b>Code:</b> <em>{q_money[0][0]}</em>\n<b>Nominal</b>: {q_money[0][1]}\n<b>Value</b>: {q_money[0][2]}')
    elif x_call_data == y_id_mass[13]:
        r_ret(z_call.message,
              f'<b>Code:</b> <em>{q_money[1][0]}\n</em><b>Nominal</b>: {q_money[1][1]}\n<b>Value</b>: {q_money[1][2]}')
    elif x_call_data == y_id_mass[14]:
        r_ret(z_call.message,
              f'<b>Code:</b> <em>{q_money[2][0]}\n</em><b>Nominal</b>: {q_money[2][1]}\n<b>Value</b>: {q_money[2][2]}')
    elif x_call_data == y_id_mass[15]:
        r_ret(z_call.message,
              f'<b>Code:</b> <em>{q_money[3][0]}\n</em><b>Nominal</b>: {q_money[3][1]}\n<b>Value</b>: {q_money[3][2]}')

