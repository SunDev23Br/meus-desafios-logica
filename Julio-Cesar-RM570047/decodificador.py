import requests
from bs4 import BeautifulSoup


def decode_secret_message(url):

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    
    text = soup.get_text("\n")

    
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    points = []

    
    # x
    # char
    # y
    i = 0

    while i + 2 < len(lines):

        try:
            x = int(lines[i])
            char = lines[i + 1]
            y = int(lines[i + 2])

            points.append((x, y, char))

            i += 3

        except ValueError:
            i += 1

    if not points:
        print("Nenhum ponto encontrado.")
        return

    max_x = max(x for x, _, _ in points)
    max_y = max(y for _, y, _ in points)

    
    grid = [
        [" " for _ in range(max_x + 1)]
        for _ in range(max_y + 1)
    ]

    
    for x, y, char in points:

        
        corrected_y = max_y - y

        grid[corrected_y][x] = char

    print("\nMensagem secreta:\n")

    for row in grid:
        print("".join(row))


decode_secret_message(
    "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
)