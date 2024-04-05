import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from random import uniform


def generate_dummy_data(traits):
    positive_scores = [uniform(0, 1) for _ in traits]
    negative_scores = [uniform(0, 1) for _ in traits]
    data = pd.DataFrame({'Trait': traits, 'Positive': positive_scores, 'Negative': negative_scores})
    return data


def generate_radar_chart(data):
    abbreviated_labels = [f"T{i+1}" for i in range(len(data['Trait']))]
    
    fig = go.Figure( )

    fig.add_trace(go.Scatterpolar(
        r=data['Positive'],
        theta=abbreviated_labels,
        text=data['Trait'],
        hoverinfo="text+r",
        fill='toself',
        fillcolor='deepskyblue',
        line=dict(color="blue"),
        name="Positive"
    ))

    fig.add_trace(go.Scatterpolar(
        r=data['Negative'],
        theta=abbreviated_labels,
        text=data['Trait'],
        hoverinfo="text+r",
        fill='toself',
        fillcolor='gold',
        line=dict(color="coral"),
        name='Negative'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1])
        ),
        width=1200,
        height=800,
        showlegend=True
    )

    st.plotly_chart(fig)


def generate_dummy_personality_data():
    personalities = ['Conscientiousness', 'Agreeableness', 'Neuroticism', 'Openness', 'Extroversion']
    percentages = [uniform(0, 1) for _ in personalities]
    data = pd.DataFrame({'Personality': personalities, 'Percentage': percentages})
    return data


def generate_bar_chart(data):
    fig = go.Figure(go.Bar(
        x=data['Personality'],
        y=data['Percentage'],
        marker=dict(color=['gold', 'coral', 'steelblue', 'plum', 'green']),
        opacity=0.90
    ))

    fig.update_layout(
        title_text='Personality Profile',
        xaxis_title='Personality Type',
        yaxis_title='Percentage'
    )

    st.plotly_chart(fig)


def main():
    st.title("YODA Report")

    st.sidebar.header("Visualization")
    visualization = st.sidebar.radio("", ("Trait Radar", "Personality Chart"))
    
    traits = [
    'Drive and Determination', 'Aggression', 'Mental Toughness', 'Conscientiousness', 
    'Responsibility', 'Leadership', 'Self-Control', 'Self Confidence', 'Coachability',
    'Truthfulness', 'Team Spirit', 'Learnability', 'Communication', 'Game Sense', 'Dangerosity',
    'Discipline', 'Drive to Improve', 'Efficiency', 'Improvement Principle', 'Motivation',
    'Obsessive Passion', 'Visual Search or Scanning', 'Achievement Motive', 'Ambition',
    'Attitude', 'Growth', 'Opportunity Principle', 'Sustained Attention', 'Work Rate',
    'Anticipation', 'Decision Making', 'Defenders\' Dilemma', 'Economy Principle', 'Judgement',
    'Sport Orientation', 'Deception Principle', 'Government', 'Cognitive Ability - Working Memory',
    'Cognitive Flexibility', 'Cognitive Functions', 'Exclusive Functions', 'Versatility',
    'Anxiety Intention and Direction', 'Belief Consistent Surprise', 'Belief Inconsistent Surprise',
    'Competence Principle', 'Composure', 'Coping', 'Ego Orientation', 'Flexibility', 'Influence',
    'In-Game Mental Pressure', 'Maturity', 'Mental Rating', 'Net Hope', 'Overall Mental Pressure',
    'Pre-Game Mental Pressure', 'Provocation', 'Surprise Principle', 'Task and Ego Orientation',
    'Mobility Principle', 'Professionalism', 'Self-Adaptor', 'Self-Concept', 'Self-Efficacy',
    'Self-Regulation', 'Volition', 'Harmonious Passion', 'Cohesion Principle', 'Presence',
    'Reserve Principle', 'Vision'
    ]

    if visualization == "Trait Radar":
        st.header("Trait Radar")
        dummy_trait_data = generate_dummy_data(traits)
        generate_radar_chart(dummy_trait_data)
    elif visualization == "Personality Chart":
        st.header("Personality Chart")
        dummy_personality_data = generate_dummy_personality_data()
        generate_bar_chart(dummy_personality_data)


if __name__ == "__main__":
    main()
