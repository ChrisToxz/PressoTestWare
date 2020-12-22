"""empty message

Revision ID: d64b2f2b79b4
Revises: 
Create Date: 2020-12-22 10:06:01.923829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd64b2f2b79b4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CalibrationModel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('brand', sa.String(length=255), nullable=True),
    sa.Column('model', sa.String(length=255), nullable=True),
    sa.Column('customer', sa.String(length=255), nullable=True),
    sa.Column('ref', sa.String(length=255), nullable=True),
    sa.Column('type_a', sa.Integer(), nullable=True),
    sa.Column('a_highValue', sa.Float(), nullable=True),
    sa.Column('a_hvPlus', sa.Float(), nullable=True),
    sa.Column('a_hvMin', sa.Float(), nullable=True),
    sa.Column('a_lowValue', sa.Float(), nullable=True),
    sa.Column('a_lvPlus', sa.Float(), nullable=True),
    sa.Column('a_lvMin', sa.Float(), nullable=True),
    sa.Column('type_b', sa.Integer(), nullable=True),
    sa.Column('b_highValue', sa.Float(), nullable=True),
    sa.Column('b_hvPlus', sa.Float(), nullable=True),
    sa.Column('b_hvMin', sa.Float(), nullable=True),
    sa.Column('b_lowValue', sa.Float(), nullable=True),
    sa.Column('b_lvPlus', sa.Float(), nullable=True),
    sa.Column('b_lvMin', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('CertificateTemplate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cert_data_1', sa.String(length=255), nullable=True),
    sa.Column('cert_data_2', sa.String(length=255), nullable=True),
    sa.Column('cert_data_3', sa.String(length=255), nullable=True),
    sa.Column('cert_data_4', sa.String(length=255), nullable=True),
    sa.Column('cert_data_5', sa.String(length=255), nullable=True),
    sa.Column('cert_data_6', sa.String(length=255), nullable=True),
    sa.Column('cert_data_7', sa.String(length=255), nullable=True),
    sa.Column('cert_data_8', sa.String(length=255), nullable=True),
    sa.Column('cert_data_9', sa.String(length=255), nullable=True),
    sa.Column('cert_data_10', sa.String(length=255), nullable=True),
    sa.Column('cert_data_11', sa.String(length=255), nullable=True),
    sa.Column('cert_data_12', sa.String(length=255), nullable=True),
    sa.Column('cert_data_13', sa.String(length=255), nullable=True),
    sa.Column('cert_data_14', sa.String(length=255), nullable=True),
    sa.Column('cert_data_15', sa.String(length=255), nullable=True),
    sa.Column('cert_data_16', sa.String(length=255), nullable=True),
    sa.Column('cert_data_17', sa.String(length=255), nullable=True),
    sa.Column('cert_data_18', sa.String(length=255), nullable=True),
    sa.Column('cert_data_19', sa.String(length=255), nullable=True),
    sa.Column('cert_data_20', sa.String(length=255), nullable=True),
    sa.Column('cert_data_21', sa.String(length=255), nullable=True),
    sa.Column('cert_data_22', sa.String(length=255), nullable=True),
    sa.Column('cert_data_23', sa.String(length=255), nullable=True),
    sa.Column('cert_data_24', sa.String(length=255), nullable=True),
    sa.Column('cert_data_25', sa.String(length=255), nullable=True),
    sa.Column('cert_data_26', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('DefaultSettings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('com', sa.String(length=255), nullable=True),
    sa.Column('main_printer', sa.String(length=255), nullable=True),
    sa.Column('label_writer', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('MainCounter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('MainCounter')
    op.drop_table('DefaultSettings')
    op.drop_table('CertificateTemplate')
    op.drop_table('CalibrationModel')
    # ### end Alembic commands ###
