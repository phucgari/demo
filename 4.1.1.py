def display_movie(m):

    print("Original name:", m["org_name"])

    print("Translated name:", m["trans_name"])

    print("year:", m["year"])

    print()

def create_movie(org_name, trans_name, year):

    return {

        "org_name": org_name,

        "trans_name": trans_name,

        "year": year

    }

movie0 = create_movie("The hunger games", "Đấu trường sinh tử",

2016)

display_movie(movie0)
def display_movie_list(m_list):

    a=len(m_list)
    for x in range(a):
        print("movie#{0}".format(x+1))

        print("original name:", m_list[x]["org_name"])

        print("translated name:",m_list[x]["trans_name"])

        print("year:",m_list[x-1]["year"])


movie_list=[]

movie0 = create_movie("The hunger games", "Đấu trường sinh tử",

2016)

movie1 = create_movie("Little Door Gods", "Tiểu Môn Thần", 2015)

movie_list.append(movie0)

movie_list.append(movie1)

display_movie_list(movie_list)


def remove_movie(m_list, movie):

    m_list.pop(m_list.index(movie))

movie0 = create_movie("The hunger games", "Đấu trường sinh tử",

2016)

movie1 = create_movie("Little Door Gods", "Tiểu Môn Thần", 2015)

movie_list = [movie0, movie1]


remove_movie(movie_list, movie0)

display_movie_list(movie_list)

def search_movie_by_year(m_list, year):
    a=[]
    for x in range(len(m_list)):
        if m_list[x]["year"]==year:
            a.append(m_list[x])
    return a
movie_list=[]

movie_list.append(create_movie("The hunger games", "Đấu trường sinh tử", 2016))

movie_list.append(create_movie("Break point", "Ranh giới chết", 2015))

movie_list.append(create_movie("Little Door Gods", "Tiểu Môn Thần", 2015))

movie_in_2015 = search_movie_by_year(movie_list, 2015)

display_movie_list(movie_in_2015)
