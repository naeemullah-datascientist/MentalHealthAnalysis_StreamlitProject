import streamlit as st

def conclusion_and_insights():
    st.title("🧠 Conclusion & Insights")

    st.markdown("""
    ## Key Insights from the Analysis

    This in-depth analysis of the **Mental Health in Tech Survey** dataset has provided crucial insights into the mental health status of professionals working in the tech industry. Our objective was to uncover key patterns, identify the main factors influencing mental well-being, and highlight the steps that can be taken to improve the workplace environment.

    ---

    ### 1. **Mental Health Outcomes in Tech**

    - **Prevalence of Mental Health Issues**: A significant portion of respondents reported mental health challenges such as anxiety, depression, and stress. This underlines the importance of prioritizing mental well-being initiatives within the tech industry.

    - **Workplace Environment**: Key factors such as **work-life balance**, **company culture**, and **management support** had a profound effect on the mental health outcomes of employees. Tech companies should focus on building a **supportive and inclusive** environment to help mitigate mental health struggles.

    ---
    
    ### 2. **Demographic Insights**

    - **Gender & Mental Health**: Female respondents exhibited higher levels of stress and burnout compared to their male counterparts, signaling the need for **targeted mental health support** for women in the tech industry.

    - **Age & Experience**: Younger professionals, particularly those early in their careers, faced more challenges with mental health. This indicates a need for **better guidance and support** for entry-level employees navigating the pressures of the tech industry.

    ---
    
    ### 3. **Key Predictors of Mental Health Struggles**

    Through our machine learning models, we identified several key features influencing mental health outcomes:

    - **Lack of Support**: Employees reporting insufficient support from management or colleagues had a higher likelihood of experiencing mental health challenges.

    - **Workload**: Long working hours and overwhelming workloads were consistently linked to negative mental health outcomes.

    - **Flexibility**: The ability to work remotely or have flexible working hours emerged as an important factor in maintaining a healthier work-life balance and mitigating stress.

    ---
    
    ### 4. **Actionable Recommendations**

    - **Implement Comprehensive Mental Health Programs**: Tech companies should develop robust mental health programs offering resources such as counseling services, workshops on stress management, and access to mental health professionals.

    - **Encourage Open Conversations**: Foster a culture of openness around mental health in the workplace. This will reduce stigma, raise awareness, and help employees feel supported.

    - **Promote Work-Life Balance**: Initiatives to enhance work-life balance, including flexible working hours and remote work opportunities, can play a pivotal role in preventing burnout.

    - **Conduct Regular Check-ins**: Regular one-on-one check-ins can help identify early signs of mental health struggles, enabling companies to provide timely support.

    ---
    
    ### 5. **Future Work**

    Further research could include **longitudinal studies** to track mental health over time and assess the effectiveness of mental health programs. Moreover, incorporating data from other industries could offer valuable insights into mental health challenges beyond the tech sector.

    ---

    ## Final Thoughts

    The insights derived from this project underscore the critical need for tech companies to take proactive steps in addressing mental health within the workplace. By identifying the key factors influencing well-being, companies can take deliberate action to **create healthier work environments**, reduce stress, and foster more productive and happier teams.

    **Let’s prioritize mental health**, ensuring employees thrive both professionally and personally. 🌟

    """)

# Call the conclusion_and_insights function in your app
if __name__ == "__main__":
    conclusion_and_insights()
