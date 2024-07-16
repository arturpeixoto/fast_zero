from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='artur', email='art@ur.com', password='minha-senha_123'
    )
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'art@ur.com'))

    assert result.username == 'artur'
    assert result.id == 1
