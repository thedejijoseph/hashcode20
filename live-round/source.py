INPUT_FILE = "f_libraries_of_the_world.txt"

import operator
def book_scanning(n_books, n_librairies, n_days, books_scores, lib_infos, lib_scores):
    
    libs = dict(enumerate(lib_infos))
    lib_books = dict(enumerate(lib_scores))

    lib_order = []
    for lib_ in lib_books.keys():
        sum_score = 0
        for book_id in lib_books[lib_]:
            sum_score += books_scores[book_id]
        lib_order.append((lib_, sum_score))
    
    new_order = []
    for lib in lib_order:
        lib_id, lib_book_score = lib
        no_of_days = libs[lib_id][1]
        new_order.append((lib_id, no_of_days, lib_book_score))
    lib_order = new_order; del new_order

    lib_order = sorted(lib_order, key=operator.itemgetter(2, 1), reverse=True)

    book_order = []
    for lib in lib_order:
        lib_id, no_of_days, sum_score = lib
        books = lib_books[lib_id]
        book_scores = [(bk, books_scores[bk]) for bk in books]

        books = sorted(book_scores, key=operator.itemgetter(1), reverse=True)
        book_ids = [bk[0] for bk in books]
        book_order.append((lib_id, book_ids))
    
    return book_order

def compute(inputFileName, outputFileName):
    file = open(inputFileName).readlines()
    (b, l, d), s = list(map(int, file[0].split())), list(map(int, file[1].split()))
    lib_i = [list(map(int, file[_].split())) for _ in range(2, 2 + l * 2, 2)]
    lib_s = [list(map(int, file[_].split())) for _ in range(3, 2 + l * 2, 2)]

    order = book_scanning(b, l, d, s, lib_i, lib_s)
    with open(outputFileName, 'w') as f:
        f.write(f'{len(order)}\n')
        for _ in order:
            lib_id, books = _
            f.write(f'{lib_id} {len(books)}\n')
            book_order = ' '.join([str(book_id) for book_id in books])
            f.write(book_order + '\n')


""" Main program """
def main(args):
    compute(args, "out/f_libraries_of_the_world.out")

main(INPUT_FILE)
