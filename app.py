from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

recipes = {
    "less_than_30": [
        {
            "name": "Garlic Butter Steak and Potatoes",
            "ingredients": [
                "1 tablespoon olive oil",
                "4 tablespoons unsalted butter divided (½ stick)",
                "1 pound Yukon Gold potatoes diced into ½-inch cubes",
                "4 cloves garlic minced",
                "1 teaspoon dried rosemary",
                "1 teaspoon dried oregano",
                "½ teaspoon kosher salt",
                "½ teaspoon ground pepper",
                "1½ pounds sirloin steak cut into 1-inch cubes",
                "Freshly chopped parsley optional for garnish"
            ],
            "instructions": [
                "Heat a cast iron skillet over medium-high heat. Add the olive oil and 2 tablespoons of the butter. Let the butter melt completely.",
                "Add the cut potatoes, garlic, rosemary, oregano, salt, and pepper. Cook for approximately 4 minutes without disturbing. Stir and cook an additional 3-4 minutes or until fork-tender. Remove the potatoes from the pan and set aside in a bowl.",
                "Return the skillet to the stove and increase the heat to high. Add 2 tablespoons of butter and stir to melt. Add the steak bites in a single layer and cook for 1 minute. Flip or stir the steak for another 1-2 minutes or until desired doneness. Remove the skillet from the heat.",
                "Add the cooked potatoes back to the skillet and toss together. Add additional salt and pepper if desired. Top with fresh chopped parsley (optional). Serve and enjoy!"
            ],
            "image": "images/1.jpeg"
        },
        {
            "name": "Air Fryer Salmon",
            "ingredients": [
                "2 salmon fillets skin-on (6-8 ounces each)",
                "2 teaspoons olive oil",
                "1 teaspoon dried oregano",
                "½ teaspoon kosher salt",
                "½ teaspoon ground black pepper",
                "½ teaspoon ground paprika",
                "½ teaspoon garlic powder"
            ],
            "instructions": [
                "Preheat an air fryer to 400°F for 5 minutes.",
                "In a small bowl, whisk the oil, oregano, salt, pepper, paprika, and garlic powder together.",
                "Brush the spice mixture on top of the salmon fillets.",
                "Set the salmon skin-side down in the preheated air fryer basket.",
                "Air fry for 8-9 minutes depending on the size of the fillets."
            ],
            "image": "images/2.jpeg"
        },
        {
            "name": "One Pan Chicken Parmesan Pasta",
            "ingredients": [
                "3 boneless skinless chicken breasts cut into cubes",
                "2 tablespoons Italian dressing (not the creamy kind)",
                "Kosher salt and freshly ground black pepper to taste",
                "16 ounces dry rigatoni pasta (1 box)",
                "24 ounces Marinara sauce store-bought or homemade",
                "½ cup freshly grated Parmesan cheese",
                "½ cup freshly shredded mozzarella cheese",
                "Chopped fresh basil optional for garnish"
            ],
            "instructions": [
                "Heat the chicken and Italian dressing in a 12-inch cast iron skillet set over medium-high heat (If you don't own a large skillet, you can use a stock pot). Season chicken with salt and pepper to taste.",
                "Cook chicken until browned and just cooked through, about 5 minutes depending on the thickness of the chicken.",
                "Add the box of pasta and the entire jar of marinara. Fill the empty marinara jar with water and add to the skillet. If using a stockpot, use 2 cups water. Lightly stir the mixture to combine.",
                "Bring the mixture to a boil and then reduce to a simmer. Cover and cook for 15 minutes or until pasta is tender to your liking (see note).",
                "Cover with grated Parmesan and then shredded mozzarella. No need to stir. Continue to cook for 2-3 more minutes or until cheese is fully melted. You can also broil the entire skillet for about 4 minutes to make the cheese extra melty!",
                "Top with chopped basil (optional) and serve! Enjoy!"
            ],
            "image": "images/3.jpeg"
        },
        {
            "name": "Baked Ground Beef Tacos",
            "ingredients": [
                "1 pound ground beef",
                "1 cup tomato puree",
                "2 tablespoons tomato paste",
                "2 teaspoons ground cumin",
                "2 teaspoons dried oregano",
                "1 teaspoon cayenne pepper",
                "1 teaspoon garlic powder",
                "1 teaspoon onion powder",
                "1 teaspoon paprika powder",
                "1.5 cups grated cheese (cheddar, gouda, or similar)",
                "12 taco shells"
            ],
            "instructions": [
                "Preheat your oven to 400°F.",
                "Heat a pan over medium-high heat, add the ground beef, and cook until the beef is no longer pink, breaking it up while cooking.",
                "Once the ground beef is cooked, add all the spices and stir.",
                "Add the tomato paste, mix it in, and keep cooking for 1 to 2 minutes (this will remove the bitterness from the tomato paste).",
                "Pour the tomato sauce into the pan, stir again, and cook for 1 – 2 minutes.",
                "Put all the taco shells in your casserole form and fill them with the ground beef mixture – 1 to 2 tablespoons each.",
                "Top with the grated cheese and bake for around 10 to 15 minutes until the cheese is melted.",
                "Serve immediately with toppings of your choice (sour cream, salsa, avocados, cilantro, tomatoes, lettuce, beans, corn…)."
            ],
            "image": "images/4.jpeg"
        },
        {
            "name": "Mexican Street Corn Dip (Elote Dip)",
            "ingredients": [
                "16 ounces low-fat cream cheese (room temperature)",
                "½ cup sour cream",
                "2 cloves garlic (minced)",
                "2 tablespoons hot sauce (I used Frank's RedHot)",
                "2 tablespoons fresh lime juice (from 1 lime)",
                "2 cups freshly shredded pepper jack cheese (divided)",
                "30 ounces canned corn (fully drained and rinsed)",
                "4 ounces low-fat feta cheese or Cotija cheese (crumbled)",
                "1 jalapeno pepper (chopped)",
                "2 tablespoons chopped red onion",
                "½ cup chopped fresh cilantro"
            ],
            "instructions": [
                "Preheat oven to 350°F. Spray a 9×13-inch baking dish with nonstick spray and set aside.",
                "In a high-powered blender or mixer, combine cream cheese, sour cream, garlic, hot sauce, lime juice, and 1 cup of the shredded cheese. Blend until fully combined.",
                "Scoop the cream cheese mixture into a large bowl and add the remaining one cup of cheese, the corn, feta, pepper, onion, and cilantro. Stir to combine.",
                "Pour the mixture into the prepared baking dish. Sprinkle with more cheese if desired.",
                "Bake for 15-20 minutes or until cheese is hot and bubbly. Garnish with more cilantro, feta, and hot sauce."
            ],
            "image": "images/5.jpeg"
        }
    ],
    "30_to_60": [
        {
            "name": "Sweet & Sour Pork with Tilda Rice",
            "ingredients": [
                "280g pork shoulder cut into bite-size pieces (around 1-inch pieces)",
                "1 tbsp light soy sauce",
                "¼ tsp white pepper",
                "Pinch salt",
                "2 garlic cloves minced",
                "½ tsp Shaoxing wine",
                "150g Tilda USA Long Grain Rice",
                "150ml water",
                "Egg whites from 1 egg",
                "1 tbsp plain flour",
                "1 tbsp cornstarch",
                "½ tbsp water",
                "Cornstarch to coat pieces",
                "1-3 cups Vegetable oil",
                "3 tbsp ketchup",
                "3 tbsp brown sugar",
                "2 tbsp white vinegar",
                "1 tbsp pineapple juice",
                "1 tsp cornstarch",
                "2 tbsp water",
                "½ red pepper cut into chunks",
                "½ green pepper cut into chunks",
                "½ white onion cut into chunks",
                "¼ cup pineapple cut into chunks (I used canned pineapple)",
                "Spring onions for garnish",
                "Sesame seeds for garnish"
            ],
            "instructions": [
                "In a bowl, add pork and rest of marinade ingredients and leave to marinate for at least 20 minutes.",
                "While pork is marinating, add the measured-out Tilda USA Long Grain Rice into a rice cooker bowl and wash it 2-3 times or until the water runs clear. Add water and cook according to instructions.",
                "In a bowl, add all the sauce ingredients and mix until combined.",
                "Mix the egg whites, plain flour, cornstarch, and water into the marinated pork until it’s evenly combined. Allow to sit for 5 minutes.",
                "Add some cornstarch in a shallow bowl and begin to coat the pieces of pork, making sure to pack the starch into the pork and shake off any excess.",
                "In a saucepan over medium-high heat, pour enough oil so it’s around 1 inch deep. Place a chopstick into the oil and if you see bubbles start to form around the chopstick, the oil is ready.",
                "Add the pork pieces into the saucepan and cook in batches for 3 minutes or until it starts to turn golden, then remove and drain on a rack.",
                "Once all cooked, turn the heat to high and double fry the pork for 1 minute until golden brown, then drain on a rack.",
                "In a wok or large skillet over medium-high heat, add some oil followed by the onions, green and red peppers, and pineapple. Stir-fry for 1 minute then remove and set aside on a plate.",
                "In the same pan, add the prepared sauce and let it come up to a rapid simmer until it starts to thicken. Add in the stir-fried vegetables and crispy pork then begin to toss to coat the pork in the sauce for around 10 seconds.",
                "Open the lid from the rice cooker and fluff up the rice with a rice spatula. Serve the saucy sweet & sour pork over the warm cooked rice. Enjoy immediately."
            ],
            "image": "images/6.jpeg"
        },
        {
            "name": "Vegetable Pilaf with Chicken Skewers",
            "ingredients": [
                "1 pouch Tilda Masala Rice",
                "1 tbsp oil",
                "1 onion finely sliced",
                "1 clove garlic crushed",
                "1 red pepper chopped",
                "50g okra sliced",
                "100g green beans cut and blanched for 4 minutes",
                "20g toasted cashew nuts",
                "Handful fresh coriander chopped",
                "Salt & black pepper to season",
                "2 large chicken breast",
                "4 tablespoons fat-free yoghurt",
                "2 tablespoons Tandoori Masala spice blend powder",
                "2 cloves garlic",
                "1 lemon"
            ],
            "instructions": [
                "Heat the oil in a large pan and add the onions, garlic, and red pepper and fry for about 5 minutes to soften.",
                "Add the okra and green beans and fry for another 5 minutes.",
                "Heat Tilda Indian Curry Rice in the microwave for 1 minute and stir into the vegetable mix.",
                "Add the cashew nuts and coriander and heat through. Season with salt and pepper and serve piping hot.",
                "For the chicken skewers, mix tandoori masala spices, fat-free yoghurt, garlic, and lemon together in a bowl.",
                "Cut the chicken breasts into even-sized cubes and marinate into the bowl for at least 10 minutes (for the best results leave the chicken to marinate in the tandoori yoghurt marinade for 2 hours).",
                "Place in a pan or in the oven and cook for 20-30 minutes until the chicken is cooked through. Don’t forget to turn the skewers halfway through cooking.",
                "Place the skewers alongside the rice and sprinkle some finely chopped coriander on top before serving."
            ],
            "image": "images/7.jpeg"
        },
        {
            "name": "Prawn Californian Rolls",
            "ingredients": [
                "250g pouch Tilda sticky rice",
                "3 tbsp seasoned rice vinegar (used Saitaku rice vinegar sweetened for sushi)",
                "3cm wasabi paste and extra to serve",
                "1 tbsp light mayonnaise",
                "75g cold water prawns drained on kitchen towel",
                "2 nori seaweed sheets",
                "15g fresh chives finely chopped",
                "1/2 small ripe avocado cut into thin batons",
                "1/8 cucumber deseeded and cut into batons",
                "Reduced salt soy sauce to serve",
                "Pickled ginger to serve"
            ],
            "instructions": [
                "Cook Tilda sticky rice according to pack instructions, stir through rice vinegar gently and spread out on a non-stick baking tray to cool completely.",
                "Mix the wasabi with the mayonnaise, add the prawns, a good grind of black pepper, and stir.",
                "Place a nori seaweed sheet long edge nearest to you on a bamboo sushi mat wrapped in cling film. With wet clean hands, spread take half of the rice and form an even thin layer of rice over two-thirds of the nori with an empty third at the top of the mat. Use a pair of sharp scissors and trim excess seaweed at the top so that there is only 2cm left where the roll will be sealed.",
                "Scatter chives over the rice and push down with the back of a spoon to stick them to it before turning the seaweed over so the rice and chives are now touching the sushi mat and the nori seaweed is facing upwards with the free 2cm still at the top of the mat.",
                "Spread half of the prawns in a horizontal line about 1cm in from where the rice starts then arrange a layer of avocado and cucumber batons on top. Use the mat to roll everything into a tight even log – rolling towards the nori without any rice on it. Use the mat to shape the log and ensure the sushi is sealed.",
                "Repeat once more with the remaining ingredients. Use a sharp knife to cut each roll into 6 even pieces then serve with the wasabi, soy sauce, and pickled ginger."
            ],
            "image": "images/8.jpeg"
        },
        {
            "name": "Aubergine Kokoro with Pickled Cabbage (Rice Bowl)",
            "ingredients": [
                "250g pouch Tilda sticky rice",
                "1 medium aubergine sliced into 1cm slices and then cut into half moons",
                "1/2 tbsp sunflower oil",
                "3 tbsp white wine vinegar",
                "1 tbsp caster sugar",
                "Good pinch of salt",
                "1/4 small or 1/8 red and white cabbages",
                "2 tbsp white miso paste",
                "1 tbsp reduced salt soy sauce",
                "1 tbsp honey",
                "80g radishes thinly sliced",
                "Small handful of coriander",
                "1 tbsp toasted unsalted peanuts chopped (or toasted sesame seeds)",
                "1 spring onion finely sliced",
                "1 red chilli thinly sliced (optional)"
            ],
            "instructions": [
                "Preheat the oven to 200°C (fan 180°C, gas 6).",
                "Place the aubergine slices on a lined baking tray, drizzle with oil, and toss the aubergine to coat lightly with oil. Roast in the oven for 15 minutes.",
                "Meanwhile, mix 100ml boiling water with the vinegar, sugar, and salt until dissolved. Mix through the cabbages and set aside to pickle, stirring frequently.",
                "Mix the miso, soy sauce, and honey together with 2 tablespoons of water, pour over the aubergine, coat well, spread out the aubergines, and cook for a further 15 minutes until sticky and tender.",
                "Cook Tilda sticky rice according to pack instructions and share between two shallow bowls. Drain the cabbage, reserving the pickling liquid, and dress the rice with some of it.",
                "Top each bowl with a pile of cabbage, some radishes, coriander, and divide the sticky miso aubergine between the bowls. Finish with peanuts (or sesame seeds), spring onions, and chilli slices if using. Add more pickling liquid to taste."
            ],
            "image": "images/9.jpeg"
        },
        {
            "name": "Vietnamese Clay Pot with Crispy Fish & Green Mango",
            "ingredients": [
                "1 clove garlic finely chopped",
                "2 tsp sunflower oil",
                "2 tomatoes quartered and the seeds removed",
                "1 lemongrass stick base chopped finely and the stalk kept whole",
                "1 spring onion cut into 3cm pieces",
                "2 Asian aubergines or 1 normal aubergine cut into 4cm long & 1cm wide pieces",
                "1 red chilli sliced into strips",
                "1½ tbsp light soy sauce",
                "1 tsp sugar",
                "1 pinch turmeric",
                "1 pinch of pepper",
                "Vietnamese basil (if available) or normal basil",
                "Fresh coriander",
                "Mint leaves",
                "2 bream",
                "6 red chillies",
                "6 tsp sugar",
                "6 tsp water",
                "6 tsp rice vinegar",
                "2 clove garlic",
                "2 green mango",
                "4 tbsp fish sauce",
                "120g Tilda Fragrant Jasmine Rice",
                "Good pinch of salt",
                "2 tbsp unsweetened desiccated coconut",
                "2 tbsp vegetable/sunflower oil",
                "Boiling water to cover the rice",
                "100ml coconut milk"
            ],
            "instructions": [
                "Put a medium saucepan on medium heat, add the oil and the garlic and fry till fragrant. Add the tomato and lemongrass base. Add 2 tbsp water and stir, simmer for 2 mins. Add 1 tbsp soy sauce and ½ tsp sugar and mix well. Add the chopped aubergine, add 150 ml of water, simmer for a minute, add the rest of the fish sauce and sugar. Mix well and add the turmeric, pepper, and the lemongrass stalk. Simmer for about 12 mins or until the aubergine is cooked. Add the spring onion and stir in. Cook for a further minute. Serve in a warm dish or clay pot and garnish with lots of chopped herbs with white rice on the side.",
                "Scale and fillet the bream, pin bone, and lightly score the fish fillets. Finely chop the chilli and garlic. Place the chilli, sugar, vinegar, fish sauce, and water in a pan and bring to the boil, reduce the heat and simmer until the mix starts to thicken, add the garlic and continue to cook until the mix is thickened. Peel and julienne the green mango. Toss in a little lime juice with a pinch of salt. Heat a frying pan until hot, season the fish skin with a little salt and cook skin-side down until crisp and golden, drizzle the skin with the glaze and then flash the fish under the grill to finish. Serve on a bed of the mango with some of the mango scattered over the top, garnish with fresh Vietnamese mint and coriander.",
                "Place the rice and coconut in a small saucepan and pour in the oil and salt, stir together. Cover the rice by 1 cm with boiling water and then bring to the boil. Reduce the heat and simmer the rice with a lid on until all the water has been absorbed. Lightly fluff the rice, stir in the coconut milk, and then place a clean tea towel over the top of the pan and recover with the lid; this will allow the rice to steam. Fluff the rice again before serving."
            ],
            "image": "images/10.jpeg"
        }
    ],
    "more_than_60": [
        {
            "name": "Apple and Cinnamon Bundt Cake",
            "ingredients": [
                "300ml Tilda Rice Milk",
                "55g dark brown soft sugar",
                "4 tsp cinnamon",
                "1/2 tsp nutmeg",
                "470g plain flour",
                "2 tsp baking powder",
                "1 tsp bicarbonate of soda",
                "1/2 tsp salt",
                "100ml oil",
                "120ml butter or plant butter melted",
                "100g light soft brown sugar",
                "100g caster sugar"
            ],
            "instructions": [
                "Preheat the oven to 175°C.",
                "Combine the dark brown sugar, cinnamon, and nutmeg in a bowl.",
                "Sieve the flour into the bowl and then add the rest of the dry ingredients apart from the light brown and caster sugar. Mix until all ingredients are evenly distributed.",
                "Combine all the wet ingredients into a separate jug.",
                "Add the caster sugar and light brown sugar to the wet ingredients and mix until dissolved.",
                "Make a well in the middle of the flour mixture and pour the wet mixture into the center. Gently mix until all the ingredients are combined. Do not over mix.",
                "Spray and flour the bundt tin and then evenly spoon the mix into the tin.",
                "Bake in the oven on a middle shelf for 60 minutes or until cooked through.",
                "Take the bundt tin out of the oven and let rest for 15 minutes. Put a plate over the top of the bundt tin and flip over. Gently remove the bundt tin.",
                "Allow to cool. Sprinkle with icing sugar and add any additional decorations. Serve on its own or with double cream."
            ],
            "image": "images/11.jpeg"
        },
        {
            "name": "Wild Rice & Broccoli Soup",
            "ingredients": [
                "240g Tilda Giant Wild Rice grains rinsed",
                "Knob of butter and extra tbsp for rice (optional)",
                "4 cloves crushed garlic/1 tbsp garlic paste",
                "1 onion diced",
                "2 cups broccoli florets roughly chopped",
                "1 cup spinach",
                "500ml milk",
                "500ml vegetable stock",
                "Salt and pepper to taste",
                "Chopped parsley (to garnish)"
            ],
            "instructions": [
                "Cook the Tilda Giant Wild Rice grains according to packet instructions. Butter is optional but can be added to the water to help separate the rice grains.",
                "In a pot, sweat an onion in butter and garlic paste on medium to high heat. Next, add the broccoli and spinach. Stir until the spinach begins to wilt. Then add the milk, vegetable stock, salt, and pepper. Stir in the giant wild rice grains, leaving some rice behind for garnishing. Cover and cook for 5-10 mins until the broccoli softens. Using a blender, blend the soup until smooth and creamy. Serve and garnish with rice grains and parsley."
            ],
            "image": "images/12.jpeg"
        },
        {
            "name": "Salmon Fish Pies",
            "ingredients": [
                "100g Tilda Brown Basmati Wholegrain Brown Basmati Rice",
                "500g salmon (organic, skin removed)",
                "400g puff pastry",
                "2 shallots finely diced",
                "2 garlic cloves crushed",
                "150g button mushrooms sliced",
                "10g chopped dill",
                "10g chopped flat leaf parsley",
                "1 lemon zested",
                "2 eggs hard boiled for 7 minutes peeled and chopped",
                "1 egg yolk beaten",
                "60g butter",
                "plain flour for dusting",
                "salt",
                "white pepper freshly ground",
                "1 shallot finely diced",
                "1 garlic clove crushed",
                "200ml fish stock",
                "200ml whipping cream",
                "60g butter",
                "50g chopped dill",
                "12 baby carrots peeled",
                "12 baby leeks trimmed",
                "60g butter",
                "30g sugar",
                "40ml pear vinegar"
            ],
            "instructions": [
                "Place the Brown Basmati rice into a saucepan, cover generously with cold water, and add a pinch of salt. Bring up to the boil, then reduce to medium heat and simmer for 20 minutes or until the rice is tender. Drain thoroughly and spread the rice out across a baking tray to cool.",
                "Preheat the oven to 180°C/gas mark 4. Meanwhile, place the salmon into a roasting tray, season generously, and place half of the butter on top of the salmon. Cover the tray with foil and cook in the oven for 8 minutes until just firm, then remove the foil and leave to cool. Flake the salmon into a bowl, taking care to remove any fish bones.",
                "Place a frying pan over low heat and gently melt the remaining butter. Add the shallots and garlic and cook without colouring for 3 minutes until softened. Add the sliced mushrooms to the pan and cook until tender, then remove from the heat and stir in the chopped herbs and lemon zest. Spread the mushroom mixture out across a baking tray to cool.",
                "Roll out the puff pastry on a lightly floured surface until 4mm thick. Cut out two 11cm discs and two 15cm discs using pastry cutters. Place the discs carefully onto a lined baking tray and chill in the fridge for 15 minutes.",
                "Meanwhile, prepare the filling. Mix the cooked salmon, rice, mushrooms, and boiled eggs together in a large bowl, seasoning to taste with salt and pepper. Line a baking tray with baking parchment and place the two smaller discs of pastry on the tray. Carefully place a mound of the salmon and rice mixture into the centre of each disc using a 9cm pastry cutter as a guide for more consistency if desired.",
                "Brush the edge of each pastry base with the egg yolk and carefully place the larger discs over the top, gently pressing down the edges to seal. Brush over the pastry top with the egg yolk to glaze and place in the fridge to chill for 20 minutes.",
                "Preheat the oven to 200°C/gas mark 6. Use a small knife to gently score semi-circular patterns down the sides to decorate, trimming the bases with a fluted cutter if desired. Pierce a steam hole in the top of each pie and bake in the oven for 20 minutes or until golden brown.",
                "Meanwhile, prepare the dill sauce. Sweat the shallot and garlic in half the butter over medium heat, then add the fish stock and continue to cook until reduced by half. Stir in the cream and bring to the boil. Once boiling, remove the pan from the heat and whisk in the remaining butter. Pass the sauce through a fine sieve and stir in the dill, seasoning to taste if necessary.",
                "For the vegetables, place the carrots in a pan and add enough water to just cover. Add half the butter and the sugar, then simmer until the carrots are tender and the water has reduced to a syrup. Add half the pear vinegar and cook for a further 20 seconds, then drain and transfer to a warmed serving dish.",
                "Repeat the process with the leeks, adding them to a pan with just enough water to cover. Add the remaining butter to the pan and cook on high heat until the leeks are tender, then add the remaining pear vinegar. Reduce until glazed and drain, adding to the serving dish with the carrots. Remove the pies from the oven and serve immediately with the glazed vegetables and dill sauce on the side."
            ],
            "image": "images/13.jpeg"
        },
        {
            "name": "Pumpkin Almond and Cheese Rice Bake",
            "ingredients": [
                "250g of Tilda Pure Basmati Rice",
                "4 shallots peeled and minced",
                "2 garlic cloves peeled and minced",
                "600g of pumpkin peeled, deseeded, and cut into 2.5cm chunks",
                "4 sprigs of thyme leaves picked",
                "75g of flaked almonds",
                "600ml of vegetable stock",
                "100g of cheddar grated",
                "1 tbsp of rapeseed oil"
            ],
            "instructions": [
                "Heat the oil in a large pan and sauté the shallots and garlic for 4–5 minutes. Add the pumpkin, thyme, and flaked almonds, and sauté for a further 8–10 minutes.",
                "Add the rice and mix well before pouring in the vegetable stock. At this point, you can continue to cook the dish in the pan covered for 20–25 minutes or bake as suggested below.",
                "Preheat the oven to 180°C/gas mark 4. To bake, spoon the mixture into a large gratin dish and scatter over ¾ of the grated cheese, cover with foil, and bake in the oven for 20 minutes. After 20 minutes, remove the foil and bake for a further 20–25 minutes until the cheese is golden brown and the rice is cooked. Serve with the remaining grated cheese, salad, and crusty bread or seasonal greens."
            ],
            "image": "images/14.jpeg"
        },
        {
            "name": "Lamb Biryani with Potatoes & Green Beans",
            "ingredients": [
                "300g Tilda Pure Basmati",
                "530g lean lamb diced",
                "30g vegetable oil",
                "3 cinnamon sticks",
                "10 cardamom pods",
                "8 cloves",
                "800ml water",
                "1 teaspoon salt",
                "200g baby potatoes boiled for 15 minutes",
                "80g green beans cooked for 5-6 minutes",
                "20g vegetable oil",
                "20g salted butter",
                "150g red onions chopped",
                "20g garlic puree",
                "40g ginger puree",
                "1 red chilli chopped",
                "1 green chilli chopped",
                "1 tbsp garam masala",
                "½ tsp ground turmeric"
            ],
            "instructions": [
                "Fry all of the masala ingredients together until soft in a large pan. Add the diced lamb and cook until sealed. In a separate pan, heat the remaining oil, add the whole spices, and heat for a few minutes. Add the rice and stir to coat with the spice mix. Add the water and salt, then combine with the lamb mix, potatoes, and green beans. Transfer to a large ovenproof casserole. Cook at 180°C (fan oven) for 50 minutes, stirring at regular intervals. Garnish with chopped coriander to serve."
            ],
            "image": "images/15.jpeg"
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest_meal():
    time = request.form['time']
    if time == "less_than_30":
        meal = random.choice(recipes["less_than_30"])
    elif time == "30_to_60":
        meal = random.choice(recipes["30_to_60"])
    else:
        meal = random.choice(recipes["more_than_60"])
    return render_template('suggest.html', meal=meal, time=time)

@app.route('/cook', methods=['POST'])
def cook_meal():
    meal_name = request.form['meal_name']
    for time_category in recipes:
        for recipe in recipes[time_category]:
            if recipe["name"] == meal_name:
                meal = recipe
                break
    return render_template('cook.html', meal=meal)

if __name__ == '__main__':
    app.run(debug=True)
