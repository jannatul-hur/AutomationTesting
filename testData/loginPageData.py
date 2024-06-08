class LoginPageData:
    test_loginPage_data = [{"email":"admin@admin.com", "password":"password"}, {"email":"kkaiser.eco@gmail.com", "password":"password"}]
    test_loginPage_data_invalid_email = [{"email":"admin@admin1.com", "password":"password"}]
    test_loginPage_data_wrong_password = [{"email": "admin@admin.com", "password": "pass"}]