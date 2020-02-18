"""创建基本数据库

Revision ID: c2616adadbc7
Revises: 
Create Date: 2019-06-14 21:51:46.909343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2616adadbc7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='排xu'),
    sa.Column('is_deleted', sa.Boolean(), nullable=True, comment='逻辑删除'),
    sa.Column('is_show', sa.Boolean(), nullable=True, comment='是否显示'),
    sa.Column('id', sa.Integer(), nullable=False, comment='ID'),
    sa.Column('name', sa.String(length=64), nullable=True, comment='部门名称'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_user',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='排xu'),
    sa.Column('is_deleted', sa.Boolean(), nullable=True, comment='逻辑删除'),
    sa.Column('is_show', sa.Boolean(), nullable=True, comment='是否显示'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('username', sa.String(length=64), nullable=True, comment='用户'),
    sa.Column('password', sa.String(length=64), nullable=True, comment='密码'),
    sa.Column('mobile', sa.String(length=64), nullable=True, comment='订单号'),
    sa.Column('department_id', sa.Integer(), nullable=True, comment='部门ID'),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tb_user_mobile'), 'tb_user', ['mobile'], unique=False)
    op.create_index(op.f('ix_tb_user_password'), 'tb_user', ['password'], unique=False)
    op.create_index(op.f('ix_tb_user_username'), 'tb_user', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tb_user_username'), table_name='tb_user')
    op.drop_index(op.f('ix_tb_user_password'), table_name='tb_user')
    op.drop_index(op.f('ix_tb_user_mobile'), table_name='tb_user')
    op.drop_table('tb_user')
    op.drop_table('department')
    # ### end Alembic commands ###
