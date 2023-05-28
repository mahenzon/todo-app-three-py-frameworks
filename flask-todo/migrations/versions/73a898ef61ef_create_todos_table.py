"""create todos table

Revision ID: 73a898ef61ef
Revises: 
Create Date: 2023-05-27 19:59:16.457068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "73a898ef61ef"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "todo_items",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("text", sa.String(length=50), nullable=False),
        sa.Column(
            "done",
            sa.Boolean(),
            server_default=sa.text("0"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("todo_items")
    # ### end Alembic commands ###
