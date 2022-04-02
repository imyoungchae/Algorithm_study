from pyvis.network import Network

net=Network()

net.add_node(1,label='hi')
net.add_node(2,label='me')
net.add_nodes(
    [3,4,5,6],
    label=['my','name','is','yc'],
    color=['#3da831','#9a31a8','#3155a8','#eb4034'],
)
net.show('list_of_nodes_with_color.html')
