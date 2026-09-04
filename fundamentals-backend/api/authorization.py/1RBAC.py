""" 

=> RBAC

    -> Role Based Access Control

    -> Is an authorization model where permission are assigned to roles and roles are 
       assigned to users


-> Why RBAC

    -> Imagine a company with 10,000 employees

    -> without RBAC

       Parveen can -> create_users , delete_users , update_users , view_reports


-> With RABC

   1. Create Role first 

       ADMIN
       HR
       Employee
       Manager 

       Then assign permision



-> Db tables 

users

id   name
-------------
1    Parveen
2    Rahul
3    Amit


roles 



id   role_name
----------------
1    Admin
2    HR
3    Employee


permissions

id    permission
-------------------------
1     create_user
2     delete_user
3     edit_salary
4     view_salary
5     apply_leave



user_roles

user_id    role_id
-------------------
1           1
2           2
3           3


role_permissions

role_id    permission_id
-------------------------
1              1
1              2
1              3
1              4

2              1
2              4

3              5




"""