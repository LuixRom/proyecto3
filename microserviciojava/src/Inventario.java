public class Inventario {
    private int id;
    private int productId;
    private int cantidad;

    public Inventario() {}
    public Inventario(int id, int productId, int cantidad) {
        this.id = id;
        this.productId = productId;
        this.cantidad = cantidad;
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public int getProductId() { return productId; }
    public void setProductId(int productId) { this.productId = productId; }

    public int getCantidad() { return cantidad; }
    public void setCantidad(int cantidad) { this.cantidad = cantidad; }
}
