"""empty message

Revision ID: f0c5b9ab393f
Revises: 
Create Date: 2024-02-17 12:13:01.159094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0c5b9ab393f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chambre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.String(length=100), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('prix', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('numero')
    )
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_client', sa.Integer(), nullable=False),
    sa.Column('id_chambre', sa.Integer(), nullable=False),
    sa.Column('date_arrivee', sa.DateTime(), nullable=False),
    sa.Column('date_depart', sa.DateTime(), nullable=False),
    sa.Column('statut', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['id_chambre'], ['chambre.id'], ),
    sa.ForeignKeyConstraint(['id_client'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    op.drop_table('client')
    op.drop_table('chambre')
    # ### end Alembic commands ###
