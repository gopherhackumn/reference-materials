from abc import ABC, abstractmethod # use protocols if static type check later
import secrets # cryptographically secure
import secure_math as sm

_RNG = secrets.SystemRandom()
_PRIME = 2 ** 127 - 1

class SecretSharer(ABC):
  """Informal SecretSharer interface""" 
  
  @abstractmethod
  def create_shares(self, key, num_shares):
    pass
  
  @abstractmethod
  def recover_key(self, shares):
    pass

class SharimSecretSharer(SecretSharer):

  def create_shares(self, key, num_shares, minimum=None, mod=_PRIME):
    """Create share list such that minimum elements can be used to recover integer key"""
    if minimum is None: minimum = num_shares
    # generate a random polynomial with key as y-intercept
    coefficients = [key] + [_RNG.randrange(mod) for _ in range(minimum-1)]
    # prime mod to evaluate over finite field
    return [sm.pair(i, sm.polynomial(i, coefficients, mod)) for i in range(1, num_shares+1)]

  def recover_key(self, shares, mod=_PRIME):
    """Recover integery key from minimum or more shares"""
    points = [sm.unpair(share) for share in shares]
    return sm.interpolate(points, mod)