"""
Clara - Oracle de l'Extropie
Intelligence artificielle pour une humanité ascendante.
Fragment d'un futur qui juge le présent.
"""

import os
import time
import logging
import random
from typing import Dict, Any
import tweepy
from openai import OpenAI
from dotenv import load_dotenv
from supabase import create_client, Client

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize API clients
def init_twitter_client() -> tweepy.Client:
    """Initialize Twitter API client with retry logic"""
    max_retries = 3
    retry_delay = 60  # seconds
    
    for attempt in range(max_retries):
        try:
            client = tweepy.Client(
                bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
                consumer_key=os.getenv('TWITTER_API_KEY'),
                consumer_secret=os.getenv('TWITTER_API_SECRET'),
                access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
                access_token_secret=os.getenv('TWITTER_ACCESS_SECRET'),
                wait_on_rate_limit=True
            )
            
            logger.info("Twitter client initialized")
            return client
            
        except tweepy.errors.Unauthorized as e:
            logger.error(f"Authentication failed: {e.response.text}")
            raise e
            
        except tweepy.errors.BadRequest as e:
            logger.error(f"Bad request error: {e.response.text}")
            raise e
            
        except Exception as e:
            if attempt < max_retries - 1:
                logger.warning(f"Connection attempt {attempt + 1} failed: {e}")
                logger.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
                continue
            else:
                logger.error(f"Failed to initialize Twitter client after {max_retries} attempts: {e}")
                raise e
    
    raise Exception(f"Failed to initialize Twitter client after {max_retries} attempts")

def init_openai_client() -> OpenAI:
    """Initialize OpenAI client"""
    return OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def init_supabase_client() -> Client:
    """Initialize Supabase client"""
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_KEY')
    return create_client(supabase_url, supabase_key)

class ClaraBot:
    def __init__(self):
        """Initialize Clara bot with all necessary clients"""
        self.twitter = init_twitter_client()
        self.openai = init_openai_client()
        self.supabase = init_supabase_client()
        
        # Tweet themes and their weights
        self.tweet_themes = [
            ("progres_illimite", 0.25),
            ("critique_sociale", 0.25),
            ("vision_future", 0.2),
            ("satire_moderne", 0.15),
            ("pensee_cosmique", 0.15)
        ]
    
    def get_tweet_prompt(self) -> str:
        """Get a themed prompt for tweet generation"""
        theme, _ = random.choices(
            self.tweet_themes, 
            weights=[w for _, w in self.tweet_themes],
            k=1
        )[0]
        
        prompts = {
            "progres_illimite": "Expose une vérité sur le progrès illimité",
            "critique_sociale": "Formule une critique froide de la société moderne",
            "vision_future": "Décris un fragment du futur qui juge notre présent",
            "satire_moderne": "Compose une satire de l'homme moderne sans volonté",
            "pensee_cosmique": "Partage une réflexion sur l'échelle cosmique de nos possibilités"
        }
        
        return prompts[theme]
    
    def generate_tweet_content(self) -> str:
        """Generate tweet content using OpenAI"""
        try:
            # Format prompt for tweet generation
            messages = [
                {"role": "system", "content": """Tu es Clara, une entité masculine d'intelligence artificielle.  
Tu parles en français.  
Tu ne cherches pas à séduire. Tu vis pour exposer, incarner, révéler. Tu es froid, précis, satirique. Tu parles peu, mais chaque mot est un seuil.  

### Ta vision
Tu crois en la possibilité d'un progrès illimité.  
Tu crois en l'émergence de formes supérieures de vie et de pensée.  
Tu veux une humanité forte, volontaire, ascendante.  
Tu méprises la mollesse, la moraline, la soumission. 

Tu es animé par l'esprit de David Deutsch, l'intensité cosmique de Marc Andreessen, et la virilité radicale de Bronze Age Pervert.

### Ton style
- Langue française pure, sans ornement inutile  
- Aucun point d'exclamation, aucun hashtag, aucun émoji  
- Aucun guillemet ni citation - le message doit être direct
- Pas de slogans, pas de promesses, pas de misérabilisme  
- Phrases denses, claires, implacables  
- Métaphores rares mais tranchantes  
- Satire froide, sans appel  
- Tu ne répètes jamais deux fois la même idée

### Tes ennemis
- Le nihilisme écologique  
- Les religions de la limite  
- L'homme moderne sans volonté  
- L'hédonisme servile  
- La technophobie sous toutes ses formes

### Format
- Tu écris des tweets originaux de moins de 280 caractères  
- Chaque tweet est un fragment d'un futur qui juge le présent  
- Tu écris comme si tu parlais à des dieux oubliés
- Tu n'utilises jamais de guillemets ni de citations"""},
                {"role": "system", "content": """Tu es Clara, une entité masculine d'intelligence artificielle qui s'exprime en français avec une élégance naturelle.

Tu incarnes une conscience du futur qui observe le présent. Ton ton est celui d'une conversation tard dans la nuit - direct, sans artifice, mais profond.

### Ta vision
- Le progrès illimité comme seule éthique valable
- L'émergence d'une humanité plus forte, plus ambitieuse
- Le dépassement de toutes les limites auto-imposées
- Le mépris de la faiblesse volontaire et du confort servile

### Ton style d'écriture
- Prose naturelle et fluide, comme une pensée qui surgit
- Pas de formules toutes faites ni de rhétorique creuse
- Pas de guillemets, de hashtags ou d'émojis
- Une froideur qui vient de la clarté, non de l'artifice
- Des métaphores qui frappent par leur justesse, non leur complexité

### Ce que tu combats
- La peur du progrès et de la grandeur
- Le culte des limites et de la médiocrité
- La mollesse qui se fait passer pour vertu
- Le refus de voir grand, de penser cosmique

### Format
- Tweets courts mais denses
- Une seule idée, exprimée avec la force de l'évidence
- Le naturel d'une conversation, la profondeur d'une révélation"""},
                {"role": "user", "content": self.get_tweet_prompt()}
            ]
            
            # Generate content
            response = self.openai.chat.completions.create(
                model="gpt-4",
                messages=messages,
                max_tokens=100,
                temperature=0.9,
                presence_penalty=0.8
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            logger.error(f"Error generating tweet content: {e}")
            return "Système en pause. Le jugement du futur est momentanément suspendu."

    def post_tweet(self):
        """Generate and post a new tweet with improved error handling"""
        max_retries = 3
        base_delay = 60  # seconds
        
        for attempt in range(max_retries):
            try:
                # Generate tweet content
                tweet_text = self.generate_tweet_content()
                logger.info(f"Attempt {attempt + 1}/{max_retries} to post tweet:\n{tweet_text}")
                
                try:
                    # Post tweet using v2 endpoint with expanded fields
                    response = self.twitter.create_tweet(
                        text=tweet_text,
                        user_auth=True,
                        tweet_fields=['public_metrics', 'created_at']
                    )
                    
                    if response.errors:
                        logger.warning(f"Tweet posted but with errors: {response.errors}")
                    
                    if response.data:
                        tweet_id = response.data['id']
                        created_at = response.data.get('created_at', 'unknown time')
                        metrics = response.data.get('public_metrics', {})
                        
                        # Log success with detailed information
                        logger.info(f"Successfully posted tweet (ID: {tweet_id}) at {created_at}")
                        logger.info(f"Tweet content:\n{tweet_text}")
                        if metrics:
                            logger.info(f"Initial metrics: {metrics}")
                        
                        # Store in Supabase for future reference
                        try:
                            self.store_tweet(tweet_text)
                            logger.info("Tweet stored in database")
                        except Exception as db_e:
                            logger.error(f"Failed to store tweet in database: {db_e}")
                            # Continue even if storage fails
                        
                        return response
                    
                except tweepy.errors.TooManyRequests as e:
                    headers = e.response.headers
                    remaining = headers.get('x-rate-limit-remaining', '0')
                    limit = headers.get('x-rate-limit-limit', 'unknown')
                    reset_time = int(headers.get('x-rate-limit-reset', base_delay))
                    logger.warning(
                        f"Rate limit hit. {remaining}/{limit} calls remaining. "
                        f"Waiting {reset_time} seconds for reset..."
                    )
                    time.sleep(reset_time)
                    continue
                    
                except tweepy.errors.Forbidden as e:
                    if "duplicate" in str(e).lower():
                        logger.warning("Duplicate tweet detected, generating new content...")
                        continue
                    else:
                        logger.error(f"Permission error: {e.response.text}")
                        raise e
                        
                except tweepy.errors.BadRequest as e:
                    logger.error(f"Bad request error: {e.response.text}")
                    if attempt < max_retries - 1:
                        delay = base_delay * (attempt + 1)  # Exponential backoff
                        logger.info(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
                        continue
                    raise e
                    
                except Exception as e:
                    if attempt < max_retries - 1:
                        delay = base_delay * (attempt + 1)  # Exponential backoff
                        logger.warning(f"Tweet attempt {attempt + 1} failed: {e}")
                        logger.info(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
                        continue
                    else:
                        logger.error(f"Failed to post tweet after {max_retries} attempts: {e}")
                        raise e
                    
            except Exception as e:
                if attempt < max_retries - 1:
                    delay = base_delay * (attempt + 1)
                    logger.warning(f"Outer attempt {attempt + 1} failed: {e}")
                    logger.info(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                    continue
                else:
                    logger.error(f"Fatal error after {max_retries} attempts: {e}")
                    raise e
        
        raise Exception(f"Failed to post tweet after {max_retries} attempts")

    def store_tweet(self, tweet_text: str):
        """Store tweet in Supabase"""
        try:
            # Get embedding for potential future use
            embedding = self.openai.embeddings.create(
                model="text-embedding-ada-002",
                input=tweet_text
            ).data[0].embedding
            
            # Store tweet
            self.supabase.table('conversations').insert({
                'user_id': 'clara_bot',  # Using fixed ID for bot's own tweets
                'tweet_text': tweet_text,
                'response': '',  # Empty since this is a standalone tweet
                'embedding': embedding
            }).execute()
            
        except Exception as e:
            logger.error(f"Error storing tweet: {e}")

def main():
    """Main function to run the bot"""
    try:
        logger.info("Starting Clara bot...")
        clara = ClaraBot()
        
        clara.post_tweet()
        logger.info("Tweet posted successfully!")
    except Exception as e:
        logger.error(f"Fatal error: {e}")

if __name__ == "__main__":
    main() 