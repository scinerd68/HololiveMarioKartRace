from mario_kart import db


class Tournament(db.Model):
    __tablename__ = 'Tournament'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    race = db.relationship('RaceDetails', backref='Tournament', lazy=True)


class Player(db.Model):
    __tablename__ = 'Player'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    current_elo = db.Column(db.Integer, nullable=False, default=1000)
    race = db.relationship('RaceDetails', backref='Player', lazy=True)


tournament_player = db.Table('TournamentPlayer',
    db.Column('tournament_id', db.Integer, db.ForeignKey('Tournament.id'), primary_key=True),
    db.Column('player_id', db.Integer, db.ForeignKey('Player.id'), primary_key=True)
)


class RaceDetails(db.Model):
    __tablename__ = 'RaceDetails'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey('Tournament.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('Player.id'), nullable=False)
    race_position = db.Column(db.Integer, nullable=False)
    player_old_elo = db.Column(db.Integer, nullable=False)
    elo_change = db.Column(db.Integer, nullable=False)
    disconnected = db.Column(db.Integer, nullable=False)