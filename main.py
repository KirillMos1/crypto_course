import tkinter, requests

url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'

root = tkinter.Tk()
root.title("CryptoCourse")
root.geometry("800x600")

style = ("Courier New", 17, "bold")
label = tkinter.Label(root, text="Name", font=style)
label.place(x = 20, y = 5)
label = tkinter.Label(root, text="Symbol", font=style)
label.place(x = 150, y = 5)
label = tkinter.Label(root, text="Price, $", font=style)
label.place(x = 250, y = 5)
label = tkinter.Label(root, text="Market Cap, $", font=style)
label.place(x = 450, y = 5)

def update():
    response = requests.get(url)
    data = response.json()
    y = 40
    for i in range(len(data)):
        if data[i]['name'] in ["Bitcoin", "Ethereum", "Solana", "Dogecoin"]:
            label = tkinter.Label(root, text=data[i]['name'], font=style)
            label.place(x = 20, y = y)
            label = tkinter.Label(root, text=data[i]['symbol'].upper(), font=style)
            label.place(x = 150, y = y)
            label = tkinter.Label(root, text=data[i]['current_price'], font=style)
            label.place(x = 250, y = y)
            label = tkinter.Label(root, text=data[i]['market_cap'], font=style)
            label.place(x = 450, y = y)
            y += 25
    root.after(1000, update)

update()

root.mainloop()
