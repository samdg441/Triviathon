def ayuda_api(self, pregunta):
    if self.ayudas_usadas >= self.total_categorias:
        print("No puedes usar más ayudas.")
        return
    self.ayudas_usadas += 1
    url = "http://api.wolframalpha.com/v2/query"
    params = {
        "input": pregunta.pregunta,
        "format": "plaintext",
        "appid": "XL5R7Q-4LAWJQJT5K",  # Tu appid
        "languagelang": "es"  # Establecer el idioma de la consulta en español
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        # Parsear la respuesta XML
        root = ET.fromstring(response.content)
        didyoumeans = root.findall(".//didyoumean")
        if didyoumeans:
            print("Wolfram Alpha sugiere:")
            for i, didyoumean in enumerate(didyoumeans, start=1):
                print(f"{i}. {didyoumean.text}")
            nueva_pregunta = input(
                "Elige una de las sugerencias o presiona Enter para intentar con otra pregunta: ")
            if nueva_pregunta:
                # Aquí puedes implementar la lógica para intentar con la nueva pregunta
                pass
        else:
            print(response.text)
    else:
        print("Error al realizar la búsqueda.")