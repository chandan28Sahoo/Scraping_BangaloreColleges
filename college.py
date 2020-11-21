from bs4 import BeautifulSoup
import requests,json,string,csv
with open("pune.html","r") as f:
    html=f.read()

soup = BeautifulSoup(html, "html.parser")

main=soup.find("div",class_="row listing-block-cont js-scrolling-container")
div=main.find_all("div",class_="top-block")


links=[]
for i in div:
    x=i.find("div",class_="clg-name-address").a["href"]
    links.append(x)


list_of_data = []
data1={}
count=0
for j in links:
    data={}
    data["link"]=j
    count+=1
    print(count)
    # print(str(count)+j)
    z=requests.get(j).text
    soup1 = BeautifulSoup(z, "html.parser")
    div=soup1.find("div",class_="college_top_wrapper")

    images=""
    college_name = ""
    ratings = ""
    reviews = ""
    estds = ""
    list_facilities=""
    contact_n0 = ""
    address = ""
    web=0
    add1=0
    x=0
    try:
        addres = soup1.find("div",class_="content_box tab-flex")
        add1 = addres.find("div",class_="lr").text
        address+=add1
        # print(address)
        contact= addres.find("div",class_="contact_block")
        cntact = contact.find_all("div",class_="lr lr_contact")
        for j in cntact:
            x=j.text.strip()
            contact_n0+=(","+x)
        # print(contact_n0)
        web_bloc = addres.find("div",class_="web_block")
        web = web_bloc.find("p",class_="lr_detail").a["href"]
        # print(web)
    except AttributeError:
        pass



    try:
        div_image=div.find("img")["src"]
        images+=(div_image)
        # print(images)

        div_n = div.find("div",class_="college_data")
        name_of_college = div_n.find("h1",class_="college_name").text
        college_name+=(name_of_college)
        # print(college_name)



        clg_ratings = div.find("div",class_="college_rating pull-right")
        ratings = clg_ratings.find("span",class_="rating_val").text
        ratings+=(","+ratings)
        # print(ratings)

        r_clg = clg_ratings.find("span",class_="rating_data")
        review = r_clg.find("a").text
        reviews+=(review)
        # print(reviews)

        facilitie = soup1.find_all("div",class_="facility")
        for i in facilitie:
            for x in i.text.strip().split():
                list_facilities+=(x+",")
        # print(list_facilities)
    except AttributeError:
        pass


    try:
        div_n = div.find("div",class_="college_data")
        extra_info = div_n.find("div",class_="extra_info")
        ex = extra_info.find_all("span")
        estd = ex[2].text.strip()
        estds+=(estd)
        # print(estds)
    except IndexError:
        pass


    
    data["college name"]=college_name
    data["Estd"] = estds
    data["Rating"] = ratings
    data["Review"] =reviews
    data["facilities"]=list_facilities
    data["image"]=images
    data["Address"]=address
    data["contact_no"]=contact_n0
    data["website"]=web
    list_of_data.append(data)
    # print(list_of_data)
    data1["result"]=list_of_data
    # print(data1)
    # if count == 5:
    #     break
    # print(data1)
    with open('colleges.json','w+') as write_file:
        json.dump(data1,write_file,indent = 4)





