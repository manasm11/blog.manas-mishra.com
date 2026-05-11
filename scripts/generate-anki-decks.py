"""
Generate Anki flashcard decks from marketing course content.
Run: python3 scripts/generate-anki-decks.py
Output: public/downloads/anki/marketing-basics.apkg
        public/downloads/anki/consumer-behavior.apkg
"""
import os
import genanki

MODEL_ID_BASICS = 1607392319
MODEL_ID_CONSUMER = 1607392320

BASIC_MODEL = genanki.Model(
    MODEL_ID_BASICS,
    "Marketing Basic",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{
        "name": "Card 1",
        "qfmt": "{{Front}}",
        "afmt": "{{FrontSide}}<hr id=answer>{{Back}}",
    }],
)

CONSUMER_MODEL = genanki.Model(
    MODEL_ID_CONSUMER,
    "Consumer Behavior Basic",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{
        "name": "Card 1",
        "qfmt": "{{Front}}",
        "afmt": "{{FrontSide}}<hr id=answer>{{Back}}",
    }],
)


def note(model, front, back):
    return genanki.Note(model=model, fields=[front, back])


def B(f, b):
    return note(BASIC_MODEL, f, b)


def C(f, b):
    return note(CONSUMER_MODEL, f, b)


# ---------------------------------------------------------------------------
# MARKETING BASICS CARDS
# ---------------------------------------------------------------------------
basics_cards = [
    # Core definitions
    B("What is Marketing?", "Satisfying consumer needs profitably."),
    B("What is a Need?", "A problem or dissatisfaction."),
    B("What is a Want?", "A solution to a need/problem."),
    B("What is Demand?", "A want along with willingness to pay.<br>Demand = Want + Willingness to pay"),
    B("What is Desire?", "A want that cannot be replaced.<br>Desire = Want + Can't be replaced"),
    B("What is Satisfaction?", "When expectations meet perceived delivery.<br>Satisfaction = Expectations − Perceived Delivery<br>(Expectations > Perceived Delivery → Dissatisfaction)"),
    B("What is Loyalty?", "When a customer wants to buy a specific product only, not substitutes."),
    B("What is Behavioral Loyalty?", "Customer buys the known brand due to inertia of change — comfortable with the known brand, doesn't look at substitutes."),
    B("What is Attitudinal Loyalty?", "Customer chooses a specific product because of a sense of belonging; feels the brand shares their core values."),
    B("What is Value (in marketing)?", "Value = ΣBenefits − ΣCosts<br>Marketer increases value by increasing benefits or decreasing costs."),

    # Go-To-Market process
    B("What are the 4 steps of a Go-To-Market Strategy?",
      "1. Need Gap Analysis<br>2. Market Scanning Analysis (5C)<br>3. Segmentation, Targeting, Positioning<br>4. Market Mix (4P/7P)"),
    B("What are the steps of the Customer Purchase Cycle?",
      "Need/Problem → Want/Solution → Demand → Desire → Satisfaction (or Dissatisfaction → back to Need) → Loyalty → Desire"),

    # Roles of Marketer
    B("What are the 5 Roles of a Marketer?",
      "1. Create Awareness of a Problem/Need<br>2. Create a Solution<br>3. Propose Value<br>4. Convert Demand to Desire (Enhance Value)<br>5. Match Expectations with Perceived Delivery"),

    # Need Gap Analysis
    B("What are the 5 types of Need Gaps a business can fill?",
      "1. Lack of Awareness of a problem/need<br>2. Lack of a Solution to a known problem<br>3. No good Value Proposition for a good solution<br>4. Possibility of Value Enhancement<br>5. Customer Expectations not being matched"),

    # Porter's 5 Forces
    B("What are Porter's 5 Forces?",
      "1. Bargaining Power of Suppliers<br>2. Bargaining Power of Buyers<br>3. Threat of Substitution<br>4. Threat of New Entrants<br>5. Extent of Rivalry"),
    B("What is the HHI (Herfindahl-Hirschman Index)?",
      "HHI = Σ(Market Share)² — measures extent of rivalry.<br>HHI &gt; 0.3 → less competitive, more profitable.<br>HHI &lt; 0.3 → more competitive, less profitable.<br>(Range 0–1 if share in fraction; 0–10,000 if in %)"),
    B("What is Monopsony?", "A market with one buyer and many suppliers. Example: satellite/missile market (government is sole buyer)."),
    B("What is Monopoly?", "A market with one supplier and many buyers. Example: radio frequency bands."),

    # PESTLE
    B("What are the 6 factors in PESTLE Analysis?",
      "1. Political<br>2. Economic<br>3. Sociocultural<br>4. Technological<br>5. Legal<br>6. Environmental (Sustainability)"),

    # Customer vs Consumer
    B("What is the difference between Customer and Consumer?",
      "Customer: buys the product (makes purchase decision).<br>Consumer: actually uses the product.<br>Example: for baby diapers, the parent is the customer, the baby is the consumer."),

    # AIDA
    B("What does AIDA stand for in the AIDA Framework?",
      "A — Awareness (of the need/problem)<br>I — Interest (look for options/alternatives)<br>D — Desire (choose/consider)<br>A — Action (buy/not buy)"),
    B("What are the consumer awareness sets in order?",
      "Awareness Set → Evoked Set → Consideration Set → Selection Set → Choice/Purchase Set"),
    B("What is an Awareness Set?", "All products/brands a consumer has ever heard about."),
    B("What is an Evoked Set?", "Top-of-mind brands/products — those with quick recall for the customer."),
    B("What is a Consideration Set?", "Products a customer actually considers buying; often influenced by friends and family."),
    B("What is a Selection Set?", "Narrowed-down handful of products a customer can buy based on price and specific needs."),
    B("What is a Choice Set (Purchase Set)?", "The final products the customer chooses to buy."),

    # CDM
    B("What are the 5 steps of the Consumer Decision Model (CDM)?",
      "1. Need/Problem Recognition (Awareness)<br>2. Search for Alternatives/Options (Intent)<br>3. Evaluation of Alternatives (Desire)<br>4. Purchase/Consumption (Action)<br>5. Post-Purchase Evaluation"),
    B("How does CDM differ from AIDA?",
      "CDM adds a 5th step: Post-Purchase Evaluation. The whole process in CDM is also governed by Culture and Personality."),

    # Attitude formation (basics.mdx section)
    B("What is the sequence of Attitude formation for a marketer to target?",
      "Attitude towards Consumption → Attitude towards Product/Category → Attitude towards Brand"),
    B("What are the 3 reasons people form attitudes?",
      "1. Value Expression<br>2. Ego Defensive<br>3. Utilitarian"),

    # Segmentation & Profiling
    B("What is Segmentation?",
      "The process of dividing customers from heterogeneous groups (different needs) into homogeneous groups (similar needs)."),
    B("What is Profiling?", "Describing and naming the clustered customer groups."),
    B("What are Psychological Variables?", "Personality + Values + Lifestyle/Behaviors"),
    B("What are the 3 Personality Types in marketing?",
      "1. Compliant — desire to belong, follow rules, need for love/belonging<br>2. Aggressive — need for achievement, success/esteem, power<br>3. Detached — break rules, need for self-actualization, do things they like"),

    # Market Sizing
    B("What is TAM (Total Addressable Market)?",
      "The total number of people globally who would be willing to buy a similar product/service."),
    B("What is SAM (Serviceable Available Market)?",
      "The subset of TAM the company can actually reach, restricted by geography and resources."),
    B("What is SOM (Serviceable Obtainable Market)?",
      "The subset of SAM the company can acquire in a given time, restricted by competition and market share potential."),
    B("When should you use a Top-Down market sizing approach?",
      "When there is a demand constraint (company can sell to all who ask). Starts from large population (TAM) down to SOM. Generally gives monetary estimates."),
    B("When should you use a Bottom-Up market sizing approach?",
      "When there is a supply constraint (expensive or resource-limited products). Starts from small-scale dynamics scaled up. Generally gives unit estimates."),

    # Positioning
    B("What is Positioning?", "The process of occupying maximum mind-space of customers."),
    B("What is Point of Parity (POP)?",
      "Characteristics similar to competitors that allow customers to trust the new product. (E.g., a new ketchup must look like ketchup.)"),
    B("What is Point of Difference (POD)?",
      "Differentiators that the new product has which can be advertised. (E.g., Maggi ketchup's sweet-and-spicy taste.)"),
    B("What is Category POP?",
      "Characteristics similar to all products in the same category, enabling trust in a new entrant."),
    B("What is Competitive POP?",
      "Characteristics similar to leading competitors specifically, enabling trust against top rivals."),

    # 4Ps
    B("What are the 4Ps of Marketing (Marketing Mix)?", "1. Product/Service<br>2. Price<br>3. Place<br>4. Promotion"),
    B("What is a Product (in marketing)?", "A bundle of features that provide benefits."),
    B("What is Goods (in marketing)?", "Product + Service"),

    # Product layers
    B("What are the 4 layers of a product/goods?",
      "1. Core Benefit — bare minimum to solve the need<br>2. Expected Product — bare minimum consumers accept as a solution<br>3. Augmented Product — additional features that differentiate from competitors<br>4. Potential Product — unknown future features that could improve the product"),
    B("What is Market Maturity?",
      "A theoretical condition where no more augmentations are possible in a product. (In practice, every product can be augmented.)"),

    # Types of Goods
    B("What are the 3 types of Goods by evaluation timing?",
      "1. Search Goods — evaluated before consumption (e.g., pen)<br>2. Experience Goods — evaluated after consumption (e.g., movie)<br>3. Credence Goods — cannot be evaluated even after consumption (e.g., educational courses, doctor's consultation)"),

    # Brand & Process
    B("What is a Brand?", "A promise or trust that a particular product makes."),
    B("What is a Process (in services)?", "Standard operating procedure."),

    # 4 service characteristics
    B("What are the 4 characteristics that make Services unique (vs Products)?",
      "1. Intangibility — cannot be measured<br>2. Variability — changes over time/place/provider<br>3. Simultaneity — production and consumption happen simultaneously<br>4. Perishability — cannot be reused/stored"),

    # Ansoff Matrix
    B("What are the 4 quadrants of the Ansoff Matrix?",
      "1. Market Penetration — existing product, existing market<br>2. Market Development — existing product, new market<br>3. Product Development — new product, existing market<br>4. Diversification — new product, new market"),
    B("What is Market Penetration Strategy?", "Increasing the consumption of existing products to existing consumers."),
    B("What is Market Development Strategy?", "Taking existing products to new markets (different geography or different segment)."),
    B("What is Product Development Strategy?", "Creating new products for existing customers/segments."),
    B("What is Diversification?", "Creating new products for new segments. Can be related (similar manufacturing) or unrelated (different manufacturing)."),

    # Product Extensions
    B("What are the 3 types of Product Extensions?",
      "1. Variant Extension — minor variants (e.g., Diet Coke)<br>2. Line Extension — major variants (e.g., Vitamin Water)<br>3. Brand Extension — entirely different product (e.g., T-Shirts)"),

    # BCG Matrix
    B("What are the 4 quadrants of the BCG Matrix?",
      "Stars: high growth, high market share — invest in marketing<br>Question Marks: high growth, low market share — risky investment<br>Cash Cows: low growth, high market share — sustain, fund stars<br>Dogs: low growth, low market share — do not invest"),

    # Distribution
    B("What is Distribution?",
      "The process by which products are transferred from Manufacturer to Consumer, and feedback and money flow back from Customer to Manufacturer."),
    B("What is Intermediation?", "Introducing a new entity into the supply chain."),
    B("What is Disintermediation?", "Removing an intermediary entity from the supply chain."),
    B("What is Reintermediation?", "Changing the intermediary entity in the supply chain."),
    B("What is Webrooming?", "Checking a product and price online, then buying offline."),
    B("What is Showrooming?", "Checking a product and price offline, then buying online."),
    B("What is a Touchpoint?", "Any interaction of a customer with a product/brand."),

    # Optimal Distribution
    B("What are the 4 Optimal Distribution Strategies?",
      "1. Direct Distribution / Vertical Marketing — high info/customization, few customers<br>2. Franchise — high info/customization, many/scattered customers<br>3. Hybrid Model — low info/customization, concentrated customers<br>4. Intensive 3rd-Party Distribution — low info/customization, scattered customers"),
    B("What is Intra-Brand Competition (Channel Conflict)?",
      "When the same product reaches the customer via different channels at different prices, leading to price reduction pressure."),
    B("What are the 2 solutions for Intra-Brand Competition?",
      "Short-Term: Make certain SKUs exclusive to certain channels.<br>Long-Term: Omni-Channel Experience — seamless experience across all touchpoints."),

    # Promotion
    B("What are Dolan's 6M Framework steps for Promotion?",
      "1. Mission — What is my objective?<br>2. Market — Who is my customer?<br>3. Message — What do I want to convey?<br>4. Medium — How can I reach them?<br>5. Money — How much resources do I need?<br>6. Measurement — How effective was the promotion?"),
    B("What are the 10 types of Advertisements?",
      "1. Regular<br>2. Ambush<br>3. Guerilla<br>4. Surrogate<br>5. Social<br>6. User Generated<br>7. Subliminal<br>8. Captive<br>9. Fear Based<br>10. Comparative"),
    B("What are the Consumer Promotion types?",
      "1. BOGO (Buy One Get One)<br>2. Premiums (something free/extra)<br>3. Bundling (mixed or pure)<br>4. Trial and Sampling"),
    B("What is the difference between Publicity and Public Relations?",
      "Publicity: organically generated, can be positive or negative.<br>Public Relations: company-induced, always positive."),

    # Pricing
    B("What is the Cost Plus Pricing formula?",
      "Price = (FixedCost / N) + VariableCost + Margin<br>Where N = estimated total units sold in lifetime."),
    B("What is Notional Loss?",
      "When a company has the potential to make more profits but doesn't — leaving money on the table."),
    B("What are the 3 strategies for pricing a new product?",
      "1. Skimming — start high, reduce over time (high-info products)<br>2. Penetration — start very low to gain market share, then raise<br>3. Going Rate — price similar to existing competitors (price-insensitive markets)"),
    B("What are the 3 degrees of Price Discrimination?",
      "1st degree: sold to highest willingness-to-pay (e.g., auction, flight tickets)<br>2nd degree: price varies by quantity (e.g., wholesale)<br>3rd degree: price varies by demographics (e.g., student discounts)"),
    B("What is Psychological Pricing?",
      "Minor price tweaks with major perception impact. Examples: pricing at ₹99 instead of ₹100 (last-digit manipulation); subtraction principle (slash-price display)."),
    B("What is Decoy Pricing?",
      "Introducing an intermediate option to nudge customers toward the more expensive option.<br>Example: The Economist's three-tier pricing where the middle option is a decoy."),
    B("What is Two-Part Pricing?",
      "Fixed part kept cheap, variable part is expensive. Example: razor (cheap) + blades (expensive); printer (cheap) + toner (expensive)."),
    B("What is Value Pricing?",
      "Increasing value by reducing price. Most common example: EDLP (Every Day Low Price)."),

    # SWOT
    B("What is the purpose of SWOT Analysis?",
      "Maps company Strengths to Opportunities they can open, and Weaknesses to Threats those weaknesses can pose. Done before entering a market."),

    # Bundling
    B("Why is Bundling a revenue maximization technique?",
      "By bundling, companies capture willingness-to-pay from customers with opposite preferences, increasing total revenue beyond selling items separately."),
    B("What is the difference between Mixed Bundling and Pure Bundling?",
      "Mixed bundling: items can also be purchased/used separately (e.g., burger + drink).<br>Pure bundling: items cannot be used separately (e.g., All-Out + refill)."),

    # Product Planning
    B("What is Product Planning?", "Ensuring the sustainability of the organization/company by planning new products."),
]

# ---------------------------------------------------------------------------
# CONSUMER BEHAVIOR CARDS
# ---------------------------------------------------------------------------
consumer_cards = [
    # Definitions
    C("What is Divestment?",
      "Consumptions that can occur only once in a lifetime. Examples: funeral services, appendicitis surgery."),
    C("What is Valence?", "The direction of drive/motivation."),
    C("What are the 3 directions Valence can take?",
      "1. Toward the Product<br>2. Toward the Process<br>3. Toward the Problem"),
    C("What is Approach Valence vs Avoidance Valence?",
      "Approach Valence: motivation toward something positive (preferred by marketers).<br>Avoidance Valence: motivation away from something negative."),
    C("What is a Grudge Purchase?",
      "A purchase made unwillingly out of necessity. Examples: condoms, insurance."),

    # EBM Model
    C("What are the steps of the Engel-Blackwell-Miniard (EBM) Consumer Decision Making model?",
      "Need → (Drive/Motivation) → Awareness Set (formed by Learning) → (Memory) → Evoked Set → (Evaluate/Perception) → Consideration Set → (Attitude) → Selection Set → Intent → Behavior"),
    C("What two factors govern the entire consumer decision-making process?",
      "1. Personality<br>2. Culture"),

    # Motivation
    C("What are the two components of Motivation?",
      "1. Problem/Need-Gap (Push factor)<br>2. Solution/Outcome Attractiveness (Pull factor)"),
    C("What are the 3 types of Motivational Conflicts?",
      "1. Approach-Approach: same value/valence for both products → Buyer's Remorse<br>2. Approach-Avoidance: wants the end result but dislikes the process<br>3. Avoidance-Avoidance: wants to avoid both the goal and the process"),
    C("How is Approach-Approach Motivational Conflict resolved?",
      "Give assurance and feedback to reduce Buyer's Remorse (consumer regret after choosing one option over another)."),
    C("How is Approach-Avoidance Motivational Conflict resolved?",
      "Change the marketing message. Example: Maggi introduced Aata Noodles to address the 'tasty but unhealthy' conflict."),

    # FAB Analysis
    C("What is FAB Analysis?",
      "Feature → Advantages/Attributes → Benefits.<br>Customers talk at the Feature level but think at the Benefits level. Marketers must understand the terminal benefit."),
    C("What is Laddering (Hierarchical Value Map)?",
      "Repeatedly asking 'Why?' to find the terminal benefit a customer seeks. Example: moisturizing cream → healthy skin → look good → confidence."),

    # Learning
    C("What are the 3 types of Learning/Conditioning?",
      "1. Classical Conditioning — learning through ads<br>2. Instrumental/Operational Conditioning — learning by doing (most effective)<br>3. Vicarious Conditioning — learning from others' experience"),
    C("How does Classical Conditioning work (Pavlov)?",
      "Neutral Stimulus (NS) + Unconditional Stimulus (US) repeated together → NS alone triggers the Unconditional Response (UR).<br>Example: 'Thanda Matlab Coca-Cola' — the phrase (NS) triggers craving (UR) without the drink."),
    C("What is Instrumental/Operational Conditioning?",
      "Learning by doing. Uses positive reinforcement (e.g., cashbacks, BOGO) or negative reinforcement (e.g., fear-based ads). Discovered by B.F. Skinner."),
    C("What is Vicarious Conditioning?",
      "Learning from others' experiences. Also called observational learning or slice-of-life advertising. Often uses brand ambassadors."),

    # Memory
    C("What are the 2 types of Memory?",
      "1. Short-Term Memory (Episodic Memory)<br>2. Long-Term Memory"),
    C("What is Encoding vs Decoding in Memory?",
      "Encoding: converting short-term memory to long-term memory (often via brand elements like jingles/logos).<br>Decoding: retrieving long-term memory through a stimulus."),
    C("What is Schema / Associated Network?",
      "Schema defines the structure of memory — how concepts are linked together in a network. Brands attach themselves to nodes (e.g., Patanjali → Traditional node). Used to identify POP, POD, and Brand Extension potential."),

    # Personality
    C("What are the 3 Personality Types in Consumer Behavior?",
      "1. Compliant — follows rules, desire to belong<br>2. Aggressive — achievement & success, need for esteem/power<br>3. Detached — breaks rules, need for self-actualization"),
    C("What is Actual Self?", "How the person is when alone, without any external influence."),
    C("What is Ideal Self?", "Who the person wants to be."),
    C("What is Social Self?", "What others think about the person."),
    C("What is Ideal Social Self?", "What the person wants others to think he/she is."),
    C("What is Multiphrenic Self?",
      "The idea that a person's self-concept shifts across social contexts (actual, ideal, social, ideal-social selves). Brands can target specific self-concepts."),

    # Personality Traits
    C("What are the 10 Personality Traits discussed in Consumer Behavior?",
      "1. Consumer Innovativeness<br>2. Variety/Novelty Seeking Behavior<br>3. Dogmatism<br>4. Need for Cognition<br>5. Consumer Ethnocentrism<br>6. Verbalization<br>7. Visualization<br>8. Outer Directedness<br>9. Inner Directedness<br>10. Optimal Stimulation Level"),
    C("What is Consumer Innovativeness?", "When a consumer uses a product in different/new ways."),
    C("What is Variety/Novelty Seeking Behavior?", "When consumers actively seek new products or features."),
    C("What is Dogmatism?",
      "Fixed beliefs that resist change. Can only be tackled by an authority figure or respected ambassador."),
    C("What is Need for Cognition?",
      "A consumer's desire to know a lot about things before deciding. High-cognition consumers respond to detailed information."),
    C("What is Consumer Ethnocentrism vs Country of Origin Effect?",
      "Country of Origin Effect: buying a product because you believe that country makes superior products (e.g., German cars for engineering).<br>Ethnocentrism: buying a product because it comes from your own group/country."),
    C("What is the Provenance Effect?",
      "A place's history of producing superior products that creates a premium/luxury association. Considered the 8th P of marketing for luxury brands."),
    C("What is Verbalization?", "Ability to comprehend through words. High verbalizers respond to text-heavy ads (articles, magazines)."),
    C("What is Visualization?", "Ability to comprehend through images. High visualizers respond to visual ads (billboards, image-heavy media)."),
    C("What is Outer Directedness?", "Desire to look good in the eyes of others."),
    C("What is Inner Directedness?", "Consuming something to please oneself."),
    C("What is Optimal Stimulation Level (OSL)?",
      "Each person has an internal activity-level frequency. A mismatch between personal OSL and environmental OSL causes discomfort. Used by the tourism industry."),

    # Perception
    C("What is Perception (in Consumer Behavior)?",
      "Perception = Stimulus Organization + Stimulus Interpretation<br>(Understand + Evaluate)"),
    C("What is Just Noticeable Difference (JND)?",
      "The minimum amount of change in a stimulus required to grab a consumer's attention. Marketers keep changes above JND to highlight, below JND to hide."),
    C("What are the 3 Perceptual Techniques marketers use?",
      "1. Figure and Ground — figure merges with or stands out from background<br>2. Grouping — creating a whole from parts<br>3. Closure — consumers fill in gaps using prior knowledge"),

    # Consumer Reactions
    C("What are the 4 Consumer Reactions to stimuli?",
      "1. Selective Attention — paying more attention to specific information<br>2. Selective Exposure — actively seeking specific knowledge<br>3. Perceptual Blocking — filtering out/ignoring stimuli<br>4. Perceptual Defense — actively denying/rationalizing away stimuli"),

    # Assimilation Contrast Theory
    C("What is the Assimilation Contrast Theory?",
      "Consumers have an expected price range. Prices within range → Assimilation Zone. Slightly outside → Plausible Zone (High or Low). Far outside → Implausible Zone (treated as a different product).<br>Assimilation/Plausible Zones create POP; Implausible Zones create POD."),

    # Attitude
    C("What is Attitude (in Consumer Behavior)?", "A learned opinion or formed disposition. Has direction (positive/negative) and magnitude (intensity)."),
    C("What is Market Creation Process?",
      "Creating awareness and positive attitude toward consumption itself (not just a product/brand). Example: Ola/Uber created attitude toward convenient taxi-hailing."),
    C("What are the 3 functions of Attitude?",
      "1. Utilitarian — likes something because it fulfils a utility (lowest involvement)<br>2. Ego-Defensive — likes something because it protects from a problem<br>3. Value-Expressive (Self-Expressive) — likes something because they can relate to it (highest involvement)"),
    C("What is the Tri-Component Model of Attitude?",
      "Attitude has 3 components:<br>1. Cognition (Know)<br>2. Affect (Feel)<br>3. Conation/Behavior (Do)"),
    C("What is the sequence of components for a High Involvement Purchase?",
      "Know → Feel → Do"),
    C("What is the sequence of components for a Low Involvement Purchase?",
      "Know → Do → Feel"),
    C("What is the sequence of components for an Impulse Purchase?",
      "Feel → Do → Know"),

    # Fishbein Model
    C("What is the Fishbein Model (Multi-Attribute Model) formula?",
      "Attitudinal Score = Σ(Belief × Importance)<br>Sums across all relevant attributes."),
    C("What are the 4 ways to improve attitude toward a product/brand?",
      "1. Add a new attribute<br>2. Increase the importance of an attribute where you are strong<br>3. Reduce the importance of an attribute where you are weak<br>4. Change the belief that you are weak on an attribute"),
    C("What is Attitude-Culture Conflict?",
      "Also called Personality-Culture Conflict. When a consumer wants to purchase a product but their culture is against it."),

    # Decision-Making Rules
    C("What are the 3 Consumer Decision-Making Rules?",
      "1. Compensatory Rule — all features evaluated; lower value on one can be offset by higher value on another<br>2. Conjunctive Rule — sets a lower cut-off for any feature; options below it are eliminated<br>3. Disjunctive Rule — sets a higher cut-off for a feature; options above it make the choice set"),
]

# ---------------------------------------------------------------------------
# Build and write decks
# ---------------------------------------------------------------------------
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "public", "downloads", "anki")
os.makedirs(OUT_DIR, exist_ok=True)

basics_deck = genanki.Deck(2059400110, "Marketing Basics")
for card in basics_cards:
    basics_deck.add_note(card)

consumer_deck = genanki.Deck(2059400111, "Consumer Behavior")
for card in consumer_cards:
    consumer_deck.add_note(card)

basics_path = os.path.join(OUT_DIR, "marketing-basics.apkg")
consumer_path = os.path.join(OUT_DIR, "consumer-behavior.apkg")

genanki.Package(basics_deck).write_to_file(basics_path)
genanki.Package(consumer_deck).write_to_file(consumer_path)

print(f"Marketing Basics:  {len(basics_cards)} cards → {basics_path}")
print(f"Consumer Behavior: {len(consumer_cards)} cards → {consumer_path}")
