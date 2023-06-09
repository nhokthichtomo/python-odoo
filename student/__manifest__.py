{
    'name': "Student",
    'summary':'student in the world',
    'description': """ """,
    'author': "Nhok",
    'website': "https://nhok.com",
    'category': 'Student in the Earth',
    'version': '1.0.2',
    'sequence': 1,
    'depends': ['base'],
    'data': [            
        'security/ir.model.access.csv',
        'security/student_security.xml',
        'views/school_view.xml',        
        'views/student_view.xml',        
        'views/language_view.xml',
        'views/student_inheritance_view.xml',
        'wizard/update_student.xml',
        #'data/test.xml',
        ],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,    
    'license': 'LGPL-3',

}
