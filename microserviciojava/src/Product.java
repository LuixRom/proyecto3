public class Product {
    private int id;
    private String name;

    public Product() {}

    public Product(int id, String name) {
        this.id = id;
        this.name = name;
    }

    // Getters y setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
