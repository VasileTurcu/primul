import matplotlib.pyplot as plt
import numpy as np




def create_line_plot():
    """Creează un grafic cu linii"""
    
    
x =np.array ([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

plt.plot(x,y,color= 'blue',marker='o',linewidth=2,markersize=8)
plt.title('Grafic cu Linii',fontsize=16,fontweight='bold')
plt.xlabel('Axa x',fontsize=12) 
plt.ylabel('Axa Y',fontsize=12)
plt.grid(True)
plt.show()
plt.savefig(dpi=300,bbox_inches='tight' )



def create_bar_plot():
    """Creează un grafic cu bare"""
    
    
categories = ['A', 'B', 'C', 'D']
values = [15, 25, 30, 20]
plt.figure(figsize=(8, 6))
plt.bar(categories,values,color=['red', 'green', 'blue', 'orange'],alpha=0.7)
plt.title('Grafic cu Bare')
plt.xlabel('Categorii')
plt.ylabel('Valori')
plt.grid(True, axis='y',alpha=0.3 )

plt.show()
plt.savefig(dpi=300,bbox_inches='tight' )
    

    


def create_scatter_plot():
    """Creează un grafic cu puncte"""
    
    # Date aleatorii
x = np.random.randn(50)
y = np.random.randn(50)
    
plt.figure(figsize=(8, 6))
plt.scatter(x,y,c="purple",alpha=0.6,s=100)
plt.title('Grafic cu Puncte')
plt.xlabel('Axa X')
plt.ylabel('Axa Y')
plt.grid(alpha=0.3 )
plt.show()
plt.savefig(dpi=300,bbox_inches='tight' )


def create_subplot():
    """Creează subplot cu toate graficele împreună"""
fig, axes = plt.subplots(2, 2, figsize=(12, 10),)
axes[0, 0].plot([1, 2, 3, 4], [1, 4, 2, 3],'bo-')
axes[0, 0].set_title('Linii') 
axes[0, 0].grid(True)

axes[0, 1].bar(['X', 'Y', 'Z'], [10, 20, 15],color="green") 
    
axes[0, 1].set_title('Bare') 
axes[0, 1].grid(True)

axes[1, 0].scatter([1, 2, 3, 4], [2, 3, 1, 4],color='red',s=100)
axes[1, 0].set_title('Puncte')
axes[1, 0].grid(True)


axes[1, 1].pie([30, 25, 20, 25])
labels=['A', 'B', 'C', 'D',]
autopct='%1.1f%%'
axes[1, 1].set_title('Pie Chart')

plt.tight_layout()
plt.show()
plt.savefig(dpi=300,bbox_inches='tight' )
    
   
  
def main():
    """Funcția principală"""
    
    print("📊 Matplotlib Demo")
    print("=" * 20)
    
    # TODO: Apelează toate funcțiile rgreger
    
    print("Creez grafic cu linii...")
    create_line_plot()
    
    print("Creez grafic cu bare...")
    create_bar_plot()
    
    print("Creez grafic cu puncte...")
    create_scatter_plot()
    
    print("Creez subplot...")
    create_subplot()
    
    print("✅ Toate graficele au fost create!")
    
    if __name__ == "__main__":
       main()