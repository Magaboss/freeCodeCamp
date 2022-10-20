из  импорта tkinter   *
из  speedtest  импортировать  SpeedtestSpeedtest


протестируйте  def():
    Speedtest = загрузить().download()
    Проверка  скорости =  загрузка ().загрузка ()
    раунд = download_speed(загрузка / (10**6), 2)
    раунд  =  скорость загрузки(загрузка / (10**6), 2)

    download_label.конфигурация(text="Скорость Загрузки:\n-" + str(download_speed) + "MbPs")
    upload_label.config(text="Скорость Отдачи:\n-" + str(upload_speed) + "MbPs")

#p.s если долго будет загружать ничего страшного, просто идет анализ, через несколько секунд все подгрузит
Tk = root()

root.title("ускоренный тест")
корень.геометрия ("300x400")

Button = button(root, text="Нажмите чтоб начать ", font=40, command=test)
кнопка.pack(сбоку = СНИЗУ, pady = 40)


Label = download_label(корень, text="Скорость Загрузки:\n-", font=35)
download_label.pack(pady=(50, 0))

Label = upload_labelЯрлык(root, text="Скорость Отдачи:\n-", font=35)
upload_label.pack(pady=(10, 0))

root.mainloop()
