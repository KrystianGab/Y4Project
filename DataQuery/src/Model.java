public class Model {
    private String name;
    private int wins;
    private int games;
    private double ratio;

    public Model(){}

    public Model(String name, int wins, int games, double ratio){
        setName(name);
        setWins(wins);
        setGames(games);
        setRatio(ratio);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getWins() {
        return wins;
    }

    public void setWins(int wins) {
        this.wins = wins;
    }

    public int getGames() {
        return games;
    }

    public void setGames(int games) {
        this.games = games;
    }

    public double getRatio() {
        return ratio;
    }

    public void setRatio(double ratio) {
        this.ratio = wins/(games-wins);
    }
}
