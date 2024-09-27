def lakoma():
    fej_t = int(input())
    test_t = int(input())
    kar_t = int(input())*2
    lab_t = int(input())*2

    legnagyobb_t = fej_t
    legnagyobb_testrész = "fej"

    if test_t > legnagyobb_t:
        legnagyobb_t = test_t
        legnagyobb_testrész = "test"

    if kar_t > legnagyobb_t:
        legnagyobb_t = kar_t
        legnagyobb_testrész = "kar"

    if lab_t > legnagyobb_t:
        legnagyobb_t = lab_t
        legnagyobb_testrész = "lab"

    return legnagyobb_testrész
