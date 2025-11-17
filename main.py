def register_catalog(filename):
    catalog = []
    with open(filename, "rt", encoding = "utf-8") as archive:
        for row in archive:
            row = row.strip()

            infos = row.split(",")

            title = infos[0]
            author = infos[1]
            year = int(infos[2])
            genre = infos[3]
            pages = int(infos[4])

            ebook = {
                "title" : title,
                "author" : author,
                "year" : year,
                "genre" : genre,
                "pages" : pages
            }

            catalog.append(ebook)
            
    return catalog

def select_genre(catalog):

    genres = []

    for ebook in catalog:
        if ebook["genre"] not in genres:
            genres.append(ebook["genre"])

    print("Genres of books listed in the catalog: \n")

    for gen in genres:
        print(f"—> {gen}")

    selected_genre = input("\nSpecify the genre you would like to consult: ")

    print()

    for ebook in catalog:
       if ebook["genre"].lower() == selected_genre.lower():
           print(f"Book Title: {ebook["title"]} | Author: {ebook["author"]}")

def calculate_average(catalog):
    total_pages = 0
    counter = 0

    for ebook in catalog:
        total_pages += ebook["pages"]
        counter += 1

    average = total_pages / counter

    print("Average number of pages in the books catalog: \n")
    print(f"{average} pages")

def sort_year(catalog):
    oldest_book = catalog[0]

    for ebook in catalog:
        if ebook["year"] < oldest_book["year"]:
            oldest_book = ebook

    print("Oldest book: \n")
    print(f"Book Title: {oldest_book["title"]} | Year of Publication: {oldest_book["year"]} ")

def min_pages(catalog):
    min = int(input("Specify the minimum number of pages required for the query: "))

    print(f"\nBooks in the catalog with more than {min} pages:\n")

    for ebook in catalog:
        if ebook["pages"] >= min:
            print(f"Book Title: {ebook["title"]} | Number of Pages: {ebook["pages"]}")

def sort_title(catalog):
    sorted_catalog = catalog[:]

    size = len(sorted_catalog)
    changed = True
    
    while changed:
        changed = False

        for i in range(size - 1):
            if sorted_catalog[i]["title"].lower() > sorted_catalog[i + 1]["title"].lower():
                sup = sorted_catalog[i]
                sorted_catalog[i] = sorted_catalog[i + 1]
                sorted_catalog[i + 1] = sup
                changed = True

    print("Catalog of books in alphabetical order:\n")

    for ebook in sorted_catalog:
        print(f"Book Title: {ebook["title"]} | Author: {ebook["author"]}")
    
    print()

filename = "books_catalog.txt"
catalog = register_catalog(filename) 
select_genre(catalog) 
print("\n-----------------------------------------------------------------------------------------------------------------------------------\n")
calculate_average(catalog) 
print("\n-----------------------------------------------------------------------------------------------------------------------------------\n")
sort_year(catalog)   
print("\n-----------------------------------------------------------------------------------------------------------------------------------\n")
min_pages(catalog) 
print("\n-----------------------------------------------------------------------------------------------------------------------------------\n")
sort_title (catalog) 