if __name__ == '__main__' :
    from domain.control import PathMannanger
    pathMannanger = PathMannanger.PathMannanger()

    import os
    import numpy as np

    import Course, ApplicationUser, CourseRepository

    import Plataform

    Plataform.Plataform(pathMannanger,
        repository = CourseRepository,
        floor = False
    )

    registration = '000001'
    password = 'abcd1234'
    courseNames = ['macro_2020_03 1']

    plataform.setApplicationUser(registration,password)
    plataform.buildPage()

    plataform.run()
