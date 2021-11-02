def make_name_dict():
    with open('./fe_name.csv', encoding='shift-jis') as f:
        data = f.readlines()
    hero = {}
    for datum in data:
        # print(datum)
        
        j_name, e_name = datum.split(',')
        try:
            name = j_name.split(' ')[1]
        except:
            print(name)
        if '箔' in name:
            continue
        if not name in hero and e_name[:-1] != '':
            hero[name] = e_name[:-1]
        else:
            continue
    return hero 

def collation_hero(file, hero):
    def __cut(d):
        return d[:-1]
    print(file)
    with open(file, 'r') as f:
        data = f.readlines()
    data = list(map(__cut, data))
    print(len(data))
    get_name = [0 for i in range(len(data))]
    for idx, datum in enumerate(data):
        for h_n in hero.keys():
            if h_n in datum:
                get_name[idx] = hero[h_n]
        if get_name[idx] == 0:
            get_name[idx] = ''
        
        
    return get_name


if __name__ == '__main__':
    hero  = make_name_dict()
    print(len(hero))

    
    rarity = 'SR+'
    file = './{}.csv'.format(rarity)
    name_list = collation_hero(file, hero)
    print(len(name_list))

    with open('convert{}.csv'.format(rarity), 'w') as f:
        for _ in name_list:
            
            f.write(_+'\n')