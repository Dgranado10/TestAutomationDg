element = driver.find_element(By.ID, "my_button")  # Localiza un botón con el ID "my_button"

element = driver.find_element(By.NAME, "username")  # Localiza un campo de texto con el nombre "username"

elements = driver.find_elements(By.CLASS_NAME, "button")  # Localiza todos los elementos con la clase "button"

elements = driver.find_elements(By.TAG_NAME, "a")  # Localiza todos los enlaces (<a>)

element = driver.find_element(By.LINK_TEXT, "Iniciar sesión")  # Localiza un enlace con el texto exacto "Iniciar sesión"

element = driver.find_element(By.PARTIAL_LINK_TEXT, "iniciar")  # Localiza un enlace que contiene la palabra "iniciar"

element = driver.find_element(By.XPATH, "//input[@id='username']")  # Localiza un input con el ID "username"

element = driver.find_element(By.XPATH, "//a[contains(text(), 'Iniciar sesión')]")  # Localiza un enlace que contiene el texto "Iniciar sesión"


#

element = driver.find_element(By.XPATH, "//input[@formControlName='username']")
element.send_keys("mi_usuario")