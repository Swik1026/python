def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "python", "c", "c+", "c#", "java")
profile("김태호", 20, "swift", "kotlin")
