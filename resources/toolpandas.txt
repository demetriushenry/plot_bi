import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt; plt.rcdefaults()

class Sample():
    def __init__(self):
        self.window = Tk()
        self.dados = None
        # tela
        self.first = []
        self.window.title("Project")
        self.window.geometry('900x300')
        lbl = Label(self.window, text="Insira sua planilha aqui: ")
        lbl.grid(column=0, row=0)
        btn = Button(self.window, text="Inserir", command=self.on_open_button_clicked)
        btn.grid(column=0, row=1)
        btn2 = Button(self.window, text="ok", command=self.create_graph)
        btn2.grid(column=5, row=1)


        self.listCombo = []
        for c in range(4):
            self.listCombo.append(self.create_comboBox(c))

        self.window.mainloop()

    def create_comboBox(self, c):
     lbl2 = Label(self.window, text="Grafico: {}".format(c+1))
     lbl2.grid(column=c+1, row=0)
     comboS = ttk.Combobox(self.window, values=self.first)
     comboS.grid(column=c+1, row=1)
     return comboS




    def get_columns(self, fname):
        self.dados = pd.read_csv(fname, sep=';', encoding='latin1')
        # dados = pd.read_excel(fname, sep=';', encoding='latin1')

        self.first = [i for i in self.dados.head(0)]

        for i in range(4):
            self.listCombo[i].config(values=self.first)

        print(self.first)


    #pandas
    def create_graph(self):
        fig, axes = plt.subplots(nrows=2, ncols=2)


        column = self.listCombo[0].get()

        #Graph1
        graph1 = self.dados.groupby(column)
        graph1[column].describe()
        self.dados[column].drop_duplicates()
        chart1 = graph1[column].aggregate(['count'])
        df1=pd.DataFrame(chart1.sort_values(['count'], ascending=False).head())
        print(df1)

        #Graph2
        column2 = self.listCombo[1].get()

        graph2 = self.dados.groupby(column2)
        graph2[column2].describe()
        self.dados[column2].drop_duplicates()
        chart2 = graph2[column2].aggregate(['count'])
        df2 = pd.DataFrame(chart2.sort_values(['count'], ascending=False).head())
        print(df2)


        #Graph3
        column3 = self.listCombo[2].get()
        graph3 = self.dados.groupby(column3)
        graph3[column3].describe()
        self.dados[column3].drop_duplicates()
        chart3 = graph3[column3].aggregate(['count'])
        df3= pd.DataFrame(chart3.sort_values(['count'], ascending=False).head())
        print(df3)

        #Graph4
        column4 = self.listCombo[3].get()
        graph4 = self.dados.groupby(column4)
        graph4[column4].describe()
        self.dados[column4].drop_duplicates()
        chart4 = graph4[column4].aggregate(['count'])
        df4= pd.DataFrame(chart4.sort_values(['count'], ascending=False).head())
        print(df4)

        ax1 = df1.plot.bar(ax=axes[0,0], rot=0)
        ax1.legend([column])

        ax2 = df2.plot.bar(ax=axes[0,1], rot=0)
        ax2.legend([column2])

        ax3 = df3.plot.bar(ax=axes[1,0], rot=0)
        ax3.legend([column3])

        ax4 = df4.plot.bar(ax=axes[1,1], rot=0)
        ax4.legend([column4])


        plt.show()



    def on_open_button_clicked(self):

     fname = filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"),
                                               ("All files", "*.*")))

     self.get_columns(fname)
     #self.window.quit()
     print(fname)

sample = Sample()