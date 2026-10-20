from tkinter import*

def Calculate():

    T= float(Thickness_entry.get())
    R= float(Insideradius_entry.get())
    A= float(Bendangle_entry.get())
    K= float(Kfactor_entry.get())

    L1=float(leg1_entry.get())
    L2=float(leg2_entry.get())

    BA=(3.14159/180)*A*(R+K*T)

    flat_lenght= L1 + L2 + BA

    Bendallowance.config(
        text=f"Bend Allowance : {BA:.2f}mm"
    )

    Flatlength.config(
        text=f"Flat Length : {flat_lenght:.2f}mm"
    )

windows=Tk()

windows.title("SheetMetal Calculation")
frame1=Frame(windows)
frame1.grid(row=7, column=0)

frame2=Frame(windows)
frame2.grid(row=8, column=0)

label_Thickness=Label(windows,
                      text="Thickness(mm):",
                      font=("Arial",10),
                      bg="#b6c2b6"
                      )
label_Thickness.grid(row=0, column=0)

Thickness_entry=Entry(windows,
                      font=("Arial",10),
                      fg="green",
                      bg="black")
Thickness_entry.grid(row=0, column=1)

label_Insideradius=Label(windows,
                         text="Inside Radius(mm):",
                         font=("Arial",10),
                         bg="#b6c2b6"
                         )
label_Insideradius.grid(row=1, column=0)
Insideradius_entry=Entry(windows,
                         font=("Arial",10),
                         fg="green",
                         bg="black")
Insideradius_entry.grid(row=1, column=1)

label_Bendangle=Label(windows,
                      text="Bend Angle(°):",
                      font=("Arial",10),
                      bg="#b6c2b6"
                      )
label_Bendangle.grid(row=2, column=0)

Bendangle_entry=Entry(windows,
                      font=("Arial",10),
                      fg="green",
                      bg="black")
Bendangle_entry.grid(row=2, column=1)

Kfactor_label=Label(windows,
                    text="K factor:",
                    font=("Arial",10),
                    bg="#b6c2b6"
                    )
Kfactor_label.grid(row=3, column=0)

Kfactor_entry=Entry(windows,
                    font=("Arial",10),
                    fg="green",
                    bg="black")
Kfactor_entry.grid(row=3, column=1)
Leg1_label=Label(windows,
                 text="Leg 1 (mm):",
                 font=("Arial",10),
                 bg="#b6c2b6"
                 )
Leg1_label.grid(row=4, column=0)
leg1_entry=Entry(windows,
                 font=("Arial",10),
                 fg="green",
                 bg="black")
leg1_entry.grid(row=4, column=1)
Leg2_label=Label(windows,
                 text="Leg 2 (mm):",
                 font=("Arial",10),
                 bg="#b6c2b6"
                 )
Leg2_label.grid(row=5, column=0)

leg2_entry=Entry(windows,
                 font=("Arial",10),
                 fg="green",
                 bg="black")
leg2_entry.grid(row=5, column=1)

Calculate_button=Button(windows,
                        text="Calculate",
                        relief="raised",
                        command=Calculate
                        )
Calculate_button.grid(row=6, column=0,
                      columnspan=2, pady=20)
Bendallowance=Label(frame1,
                    text="Bend Allowance:",
                    font=("Arial",10),
                    bg="#b6c2b6"
                    )
Bendallowance.pack()

Flatlength=Label(frame2,
                 text="Flat Lenght:",
                 font=("Arial",10),
                 bg="#b6c2b6"
                 )
Flatlength.pack()

windows.config(background="#b6c2b6")

icon=PhotoImage(file="Sheetmeteal.png")
windows.iconphoto(True,icon)

windows.mainloop()