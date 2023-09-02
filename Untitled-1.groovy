
DbObject{
    Id:
    StateId:
    ClassId:
    ClassName:
    createDate
    lastUpdate
    createUserId
    updateUserId
}


User - Аккаунт


Person(DbObject){
    FirstName
    LastName
    Patronymic
    DateOfBirth
    Gender
    PhoneNumber
    Email
    Address
}
Parents(Person)- Родители
Students(Person) - Студенты
Teachers(Person)- преподователи



Component(DbObject){
    caption
    description
    fullInfo
    files[]
    iamges[]
    imageCategories[]
    fileCategories[]
}

News(Component)
Awards(Component)
Advantages(Component)
Comments(Component)
Courses(Component)
Professions(Component)
Stakeholders(Component)

MediaCategory(DbObject){
    caption,
    description,
    name,
    items[]
}

ImageCategory(DbObject){}
FileCategory(DbObject){}


ComponentImageCategories(ImageCategory){
    CompoentId;
}

ComponentFileCategories(FileCategory){
    ComponentId;
}



File(DbObject){
    caption,
    name,
    fileName,
    size,
    extension,
    file
    categoryId
}


Image(File){
    width,
    categoryId,
    height,
    alt
}

ComponentImage(Image){
    ComponentId;
}

ComponentFile(File){
    ComponentId;
}



WebOrders
Questions