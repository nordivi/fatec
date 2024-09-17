public class Usuarios {
    private String login;
    private String senha;
    private int id_cli; 
    
    public Usuarios(String login, String senha, int id_cli) {
        this.login = login;
        this.senha = senha;
        this.id_cli = id_cli;
    }
    
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public int getIdCli() {
        return id_cli;
    }

    public void setIdCli(int id_cli) {
        this.id_cli = id_cli;
    }
}