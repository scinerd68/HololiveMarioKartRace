from mario_kart import db


class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    race = db.relationship('RaceDetails', backref='tournament', lazy=True)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    current_elo = db.Column(db.Integer, nullable=False, default=1000)
    race = db.relationship('RaceDetails', backref='player', lazy=True)


tournament_player = db.Table('TournamentPlayer',
    db.Column('tournament_id', db.Integer, db.ForeignKey('tournament.id'), primary_key=True),
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True)
)


class RaceDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    race_position = db.Column(db.Integer, nullable=False)
    elo_change = db.Column(db.Integer, nullable=False)
    disconnected = db.Column(db.Integer, nullable=False)